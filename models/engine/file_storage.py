#!usr/bin/python3
"""
File Storage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        Args:
            obj: object to add
        """
        ind = obj.__class__.__name__ + "." + obj.id
        self.__objects[ind] = obj

    def save(self):
        """
        Serializes __objects attribute to JSON file
        """
        dicti = {}
        for x in self.__objects:
            dicti[x] = self.__objects[x].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dicti, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects attribute
        """
        try:
            with open(self.__file_path, "r") as f:
                jo = json.load(f)
            for obj in jo.values():
                cls_name = obj["__class__"]
                del obj["__class__"]
                self.new(eval(cls_name)(**obj))
        except:
            pass
