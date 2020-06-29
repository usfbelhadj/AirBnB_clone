#!/usr/bin/python3


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def default(self, line):
        pass

    def do_quit(self, line):
        """Exits the program.
        """
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    help_EOF = help_quit
    do_EOF = do_quit

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
