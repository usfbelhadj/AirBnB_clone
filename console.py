#!/usr/bin/python3
""" entry point of the command interpreter"""


import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
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
        """Check Classes"""
        if class_name == '':
            print('** class name missing **')
            return False
        if class_name != 'BaseModel' and class_name != 'User' and class_name != 'State' and class_name != 'Review' and class_name != 'Amenity' and class_name != 'Place' and class_name != 'City':
            print("** class doesn't exist **")
            return False
        return True

    def do_create(self, arg):
        """Create"""
        if self.check_class(arg):
            if arg == 'BaseModel':
                new_model = BaseModel()
            if arg == 'User':
                new_model = User()
            if arg == 'State':
                new_model = State()
            if arg == 'Place':
                new_model = Place()
            if arg == 'City':
                new_model = City()
            if arg == 'Amenity':
                new_model = Amenity()
            if arg == 'Review':
                new_model = Review()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """Show"""
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
        """Destroy"""
        args = arg.split(' ')
        if self.check_class(args[0]):
            if len(args) < 2:
                print('** instance id missing **')
                return
            if args[1] == '':
                print('** instance id missing **')
                return
            dic = "{}.{}".format(args[0], args[1])
            if dic not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[dic]
                storage.save()

    def do_all(self, arg):
        """Show All"""
        t = []
        if arg == '':
            for k, v in storage.all().items():
                t.append(str(v))
        elif arg == 'BaseModel' or arg == 'User' or arg == 'State':
            for k, v in storage.all().items():
                if arg in k:
                    t.append(str(v))
        else:
            print("** class doesn't exist **")
            return
        print(t)

    def do_update(self, arg):
        """Update"""
        args = arg.split(' ')
        if self.check_class(args[0]):
            if len(args) < 2:
                print('** instance id missing **')
                return
            if args[1] == ' ':
                print('** instance id missing **')
                return
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            v = objects[key]
            v.__dict__[args[2]] = args[3]
            v.save()

    def do_count(self, arg):
        """Counts"""
        args = arg.split(' ')
        if self.check_class(args[0]):
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
        else:
            for k in storage.all():
                print(k)
                if k.startswith(args[0] + '.'):
                    print(len(k))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
