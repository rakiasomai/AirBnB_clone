#!/usr/bin/python3
import shlex
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    classes = ["BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"]
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Quit command to exit the program
        """
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        objectt = eval(arg)()
        print(objectt.id)
        objectt.save()
        storage.save()

    def do_show(self, arg):
        arg = shlex.split(arg)
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        try:
            key = arg[0] + "." + arg[1]
            value = models.storage.all()[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        arg = shlex.split(arg)
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        try:
            key = arg[0] + "." + arg[1]
            models.storage.all()[key]
            models.storage.all().pop(key)
            models.storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        if len(arg) == 0:
            obj = storage.all()
            doc = []
            for i in obj.values():
                doc.append(str(i))
            print(d)
        elif arg in HBNBCommand.classes:
            obj = storage.all()
            doc = []
            for i in obj.values():
                if i.__class__.__name__ == arg:
                    doc.append(str(i))
            print(doc)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        arg2 = arg.split('"')
        arg1 = arg.split()
        if len(arg1) == 0:
            print("** class name missing **")
            return False
        if arg1[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(arg1) == 1:
            print("** instance id missing **")
            return False
        k = arg1[0] + "." + arg1[1]
        object = storage.all()
        if k not in object:
            print("** no instance found **")
            return False
        if len(arg1) == 2:
            print("** attribute name missing **")
            return False
        if len(arg1) == 3:
            print("** value missing **")
            return False
        try:
            type_v = type(getattr(object[k], arg1[2]))
            setattr(object[k], arg1[2], type_v(arg2[1]))
        except:
            setattr(object[k], arg1[2], arg2[1])
        storage.save()
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
