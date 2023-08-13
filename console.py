#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class

    Attributes:
        prompt(str): the prompt
        classesnames(dict): all classes
    """
    prompt = '(hbnb) '
    file = None
    classesnames = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    @staticmethod
    def ReshapeCommand(s):
        """ convert <class name>.<command>() to <command> <class name>

        Args:
        s(str): string to reshape
        """
        if not re.match(r'\s*\w+\.\w+\(.*\)\s*$', s):
            # print("not a valid command")
            return [s]
        valid_comd_list = []
        fs = s.split(".")
        first = fs[0].lstrip()
        function_args = s[s.find("(") + 1:s.rfind(")")].strip()
        second = fs[1].split("(")[0]
        args = ""
        if function_args != "":
            try:
                args_dic = eval(function_args)
                if isinstance(args_dic, tuple):
                    for e in args_dic:
                        s_e = e
                        if isinstance(e, dict):
                            for k, v in e.items():
                                comand = f'{second} {first} '
                                comand += f'{args_dic[0]} {gvs(k)} {gvs(v)}'
                                valid_comd_list.append(comand)
                            return valid_comd_list
                        args += f' {gvs(str(s_e))}'
                else:
                    args += str(args_dic)
            except Exception as e:
                # print("can't parse function args:" + str(e))
                return [s]
        valid_comd_list.append(f"{second} {first} {args}")
        return valid_comd_list

    def splitter(self, ss, delimter=" \t\n\v\r\f"):
        """split string according to delimter

        Args:
        ss(str): string
        delimter(str): delimter
        """
        list_of_strings = []
        oneword = ""
        inside_quote = False
        for i in range(len(ss)):
            c = ss[i]
            if c == '"':
                if ss[i - 1] != "\\":
                    if inside_quote:
                        inside_quote = False
                    else:
                        inside_quote = True
                    continue
                else:
                    pass
            if c in delimter and not inside_quote:
                if (oneword != ""):
                    list_of_strings.append(oneword)
                oneword = ""
                continue
            if c != "\\":
                oneword += c
        if len(oneword) != 0:
            list_of_strings.append(oneword)
        return list_of_strings

    def do_quit(self, line):
        """Quit to exit the program

        Args:
        line(str): string
        """
        print("")
        return True

    def do_EOF(self, line):
        """EOF to exit the program

        Args:
        line(str): string
        """
        print("")
        return True

    def emptyline(self):
        """
        Disables the repetition of the last command
        """
        pass

    def do_create(self, _args):
        """Creates a new instance from class name

        Args:
        _args(str): string
        """
        args = self.splitter(_args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classesnames:
            print("** class doesn't exist **")
        else:
            print(HBNBCommand.classesnames[args[0]]().id)
            models.storage.save()

    def do_show(self, _args):
        """Prints the string representation of an instance based class/id

        Args:
        _args(str): string"""
        args = self.splitter(_args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classesnames:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in models.storage.all():
            print("** no instance found **")
        else:
            print(models.storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, _args):
        """Deletes an instance based on the class name and id

        Args:
        _args(str): string"""
        args = self.splitter(_args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classesnames:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in models.storage.all():
            print("** no instance found **")
        else:
            models.storage.all().pop(f"{args[0]}.{args[1]}")
            models.storage.save()

    def do_all(self, _args):
        """Prints all string representation of all instances

        Args:
        _args(str): string"""
        args = self.splitter(_args)
        if len(args) == 0:
            # prints all
            ss = []
            for k, v in models.storage.all().items():
                ss.append(str(v))
            print(ss)
        elif args[0] not in HBNBCommand.classesnames:
            print("** class doesn't exist **")
        else:
            # prints specific class
            ss = []
            for k, v in models.storage.all().items():
                if args[0] == v.__class__.__name__:
                    ss.append(str(v))
            print(ss)

    @staticmethod
    def CastedToType(v):
        """convert string to int or float or keep it a string

        Args:
        _args(str): string"""
        try:
            v = int(v)
            # print("it's a int")
        except ValueError:
            try:
                v = float(v)
                # print("it's a float")
            except ValueError:
                # print("it's a string")
                pass
        return v

    def do_update(self, _args):
        """Updates an instance based on the class name and id

        Args:
        _args(str): string"""
        args = self.splitter(_args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classesnames:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in models.storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = models.storage.all()[f"{args[0]}.{args[1]}"]
            setattr(obj, args[2], self.CastedToType(args[3]))
        models.storage.save()

    def do_count(self, _args):
        """count instances's number of a class

        Args:
        _args(str): string"""
        args = self.splitter(_args)
        nb = 0
        for k, v in models.storage.all().items():
            if args[0] == v.__class__.__name__:
                nb += 1
        print(nb)

    def default(self, _args):
        """default commands handling

        Args:
        _args(str): string"""
        all_cmd = self.ReshapeCommand(_args)
        if (all_cmd == [_args] or all_cmd == []):
            print(f"*** Unknown syntax: {_args}")
            return False
        for cm in all_cmd:
            self.onecmd(cm)


def gvs(ss):
    """quote the string when there is a whitespace in it

        Args:
        ss(str): string"""
    if not isinstance(ss, str):
        return ss
    for c in ss:
        if c.isspace() and (ss[0] != '"' or ss[-1] != '"'):
            return f'"{ss}"'
    return ss


if __name__ == '__main__':
    HBNBCommand().cmdloop()
