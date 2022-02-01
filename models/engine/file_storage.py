#!usr/bin/python3
"""
File Storage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    FileStorage class
    Attributes:
        self.__file_path: path to the JSON file
        self.__objects: dictionary of objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary object
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        Args:
            obj: object to add
        """
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """
        Serializes __objects attribute to JSON file
        """
        dicti = FileStorage.__objects
        obj_dict = {obj: dicti[obj].to_dict() for obj in dicti.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects attribute
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass

    def classes(self):
        """
        Returns the list of class names
        """
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity
        }
        return classes
