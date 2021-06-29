#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the actions the user can do inside of the console"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        """Overrides default emptyline method"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
