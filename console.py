#!/usr/bin/python3
"""
console 0.0.1
"""


from ast import Return
import cmd
from models.base_model import BaseModel
from models import storage

classes = {
    "BaseModel": BaseModel,
}
class_list = []
for key in classes:
    class_list.append(key)
commands = [
    "do_create",
    "do_show",
    "do_destroy",
    "do_all",
    "do_update",
]


class HBNBCommand(cmd.Cmd):
    """comand interpreter file"""
    prompt = "(hbhb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program"""
        return True

    def emptyline(self):
        """Handles empty spaces when you press ENTER"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if args == "":
            print("** class name missing **")
        else:
            if args not in class_list:
                print("** class doesn't exist **")
            else:
                new_instance = classes[args]()
                print(new_instance.id)
                new_instance.save()

    def do_show(self, args):
        """Prints string representation of an instance"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()

    def do_all(self, args):
        """Prints string representation of all instances"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                print(storage.all())

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        if len(args) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                args[2] = args[2].split("=")
                                setattr(storage.all()[key],
                                        args[2][0], args[2][1])
                                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
