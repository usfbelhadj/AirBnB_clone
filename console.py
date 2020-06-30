#!/usr/bin/python3
""" entry point of the command interpreter"""


import cmd
import json
from models.base_model import BaseModel
from models import storage
from datetime import datetime


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
            if len(args) < 2:
                print('** instance id missing **')
                return
            if args[1] == '':
                print('** instance id missing **')
                return
            for i, v in storage.all().items():
                i = i.split('.')
                if args[1] == i[1]:
                    print(v)
                    return
            print("** no instance found **")
            
    def do_destroy(self, arg):
        pass
            

    def do_all(self, arg):
        t = []
        if arg == '':
            for k, v in storage.all().items():
                t.append(str(v))
        elif arg == 'BaseModel':
            for k, v in storage.all().items():
                if arg in k:
                    t.append(str(v))
        else:
            print("** class doesn't exist **")
            return
        print(t)






if __name__ == '__main__':
    HBNBCommand().cmdloop()
