#!/usr/bin/python3

"""
    Module - console
    Entry point of the cmd interpreter
"""


import cmd

class HBNBCommand(cmd.Cmd):
    """Initializing the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()