#!/usr/bin/python3

"""
    Module - console
    Entry point of the cmd interpreter
"""


import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import storage 

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
    
    # Maping class names to their respective classes
    classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def do_create(self, arg):
        """Create a new instance and save it. Print the instance id."""

        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[class_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string represantion of an instance."""
        
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        if args[0] not in self.classes:
             print("** class doesn't exist **")
             return

        if len(args) < 2:
            print("** instance id missing **")
            return
        
        obj_key = args[0] + '.' + args[1]
        objects = storage.all()
        if obj_key in objects:
            print(objects[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance"""

        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        if args[0] not in self.classes:
             print("** class doesn't exist **")
             return

        if len(args) < 2:
            print("** instance id missing **")
            return
        
        obj_key = args[0] + '.' + args[1]
        objects = storage.all()
        if obj_key in objects:
            del objects[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all instances"""

        args = shlex.split(arg)
        if not arg or args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        instance_list = [str(v) for k, v in objects.items() if k.split('.')[0] == args[0]]
        print(instance_list)

    def do_update(self, arg):
        """Update an instance"""

        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = args[0] + '.' + args[1]
        objects = storage.all()
        if obj_key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]
        instance = objects[obj_key]
        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass
        setattr(instance, attr_name, attr_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
