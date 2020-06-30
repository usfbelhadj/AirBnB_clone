#!/usr/bin/python3
""" entry point of the command interpreter"""


import cmd
import json
from models.base_model import BaseModel

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
        
    def check_class(self, class_name):
        if class_name == '':
            print('** class name missing **')
            return False
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return False
        return True


    def do_create(self, arg):
        if self.check_class(arg):
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)



    def do_show(self, arg):
        args = arg.split(' ')
        if self.check_class(args[0]):
            if args[1] == '':
                print('** instance id missing **')
            with open("file.json", "r", encoding="utf-8") as f:
                obj = json.load(f)
                for i, v in obj.items():
                    for x, y in v.items():
                        if (x == 'id'):
                            if args[1] == y:
                                def __str__(self):
                                    return ("[{}] ({}) {}".format
                                            (type(self).__name__, self.id, self.__dict__))
                            else:
                                print("** no instance found **")
                                


if __name__ == '__main__':
    HBNBCommand().cmdloop()
