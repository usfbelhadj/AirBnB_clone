#!/usr/bin/python3
""" entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb) '

    def default(self, line):
        """default"""
        pass

    def do_quit(self, line):
        """Exits the program"""
        return True

    def help_quit(self):
        """help quit"""
        print("Quit command to exit the program")

    help_EOF = help_quit
    do_EOF = do_quit

    def emptyline(self):
        """empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
