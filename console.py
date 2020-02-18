#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    classes = ["BaseModel", "User"]
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
        if arg == '':
            print("** class name missing **")
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objectt = eval(arg)()
            print(objectt.id)
            objectt.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
