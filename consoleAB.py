#!/usr/bin/python3
"""
The console
"""
from datetime import datetime
import cmd
import models
import re
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

classes = {
    'Amenity': Amenity, 'BaseModel': BaseModel, 'City': City,
    'Place': Place, 'Review': Review, 'State': State, 'User': User
}

list_of_classes = []
for key in classes:
    list_of_classes.append(key)


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_EOF(self, args):
        """Exits console"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """
        When an empty line is entered in response to the prompt,
        it won't repeat the last nonempty command entered.
        """
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel and saves it"""
        if args == "":
            print("** class name missing **")
        else:
            if args not in list_of_classes:
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
            if args[0] not in list_of_classes:
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
            if args[0] not in list_of_classes:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0]+"." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()

    def do_all(self, args):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args = args.split()
        if len(args) > 0 and args[0] not in list_of_classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(args) > 0 and args[1] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(args) == 0:
                    objl.append(obj.__str__())
                print(objl)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in list_of_classes:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    instan_data = storage.all().get(key)
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        if len(args) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                setattr(instan_data, args[2], args[3])
                                setattr(instan_data, 'updated_at',
                                        datetime.now())
                                storage.save()

    def do_count(self, args):
        """ count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        args = args.split()
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def get_objects(self, instance=''):
        """Gets the elements created by the console
        This method takes care of obtaining the information
        of all the instances created in the file `objects.json`
        that is used as the storage engine.
               """
        objects = models.storage.all()
        if instance:
            # keys = objects.keys()
            return [str(val) for key, val in objects.items()
                    if key.startswith(instance)]
        return [str(val) for key, val in objects.items()]

    def default(self, line):
        """
        by using regular expression we will search for an pattern "."
        "<class name>.<method name>" or not,
        and links it to the corresponding method in case the
        class exists and the method belongs to the class.
        """
        if '.' in line:
            splitted = re.split(r'\.|\(|\)', line)
            class_name = splitted[0]
            method_name = splitted[1]
            if class_name in list_of_classes:
                if method_name == 'all':
                    print(self.get_objects(class_name))
                elif method_name == 'count':
                    print(len(self.get_objects(class_name)))
                elif method_name == 'show':
                    class_id = splitted[2][1:-1]
                    self.do_show(class_name + ' ' + class_id)
                elif method_name == 'destroy':
                    class_id = splitted[2][1:-1]
                    self.do_destroy(class_name + ' ' + class_id)



if __name__ == '__main__':
    HBNBCommand().cmdloop()