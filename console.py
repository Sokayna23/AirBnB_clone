#!/usr/bin/python3
"""Console module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    file = None

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




if __name__ == '__main__':
    HBNBCommand().cmdloop()
