#!/usr/bin/python3
"""Console module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    file = None

    def do_quit(self, line):
        """Exit the program"""
        exit()

    def do_EOF(self, line):
        return True




if __name__ == '__main__':
    HBNBCommand().cmdloop()
