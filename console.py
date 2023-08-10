#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    file = None
    classesnames = {"BaseModel":BaseModel}

    def do_quit(self, line):
        """Quit to exit the program"""
        print("")
        return True

    def do_EOF(self, line):
        """EOF to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Disables the repetition of the last command"""
        pass
    
    def do_create(self, _args):
        """Creates a new instance from class name"""
        args = _args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classesnames:
            print("** class doesn't exist **")
        else:
            print(HBNBCommand.classesnames[args[0]]().id)
            models.storage.save()
    def do_show(self, _args):
        """Prints the string representation of an instance based on the class name and id"""
        args = _args.split()
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
        """Deletes an instance based on the class name and id"""
        args = _args.split()
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
        """Prints all string representation of all instances based or not on the class name"""
        args = _args.split()
        if len(args) == 0:
            # prints all
            ss = []
            for k,v in models.storage.all().items():
                ss.append(str(v))
            print(ss)
        elif args[0] not in HBNBCommand.classesnames:
            print("** class doesn't exist **")
        else:
            # prints specific class
            ss = []
            for k,v in models.storage.all().items():
                if args[0] == v.__class__.__name__:
                    ss.append(str(v))
            print(ss)
            
            




if __name__ == '__main__':
    HBNBCommand().cmdloop()
