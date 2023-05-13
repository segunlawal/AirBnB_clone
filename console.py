#!/usr/bin/python3
"""This module contains the HBNBCommand"""
import cmd


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit with EOF"""
        return True

    def help_quit(self):
        """Help message to quit command"""
        print("Quit command to exit the program")

    def emptyline(self):
        """Do nothing with an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
