#!/usr/bin/python3
"""This module contains the FileStorage class"""
import json
from importlib import import_module
import datetime


class FileStorage:
    """This class serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects.update({key: obj})

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, mode="w") as objf:
            dict_storage = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict_storage, objf)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                the_classes = {
                        'BaseModel': "base_model",
                        'User': "user",
                        'State': "state",
                        'City': "city",
                        'Amenity': "amenity",
                        'Place': "place",
                        'Review': "review"
                }
                for value in data.values():
                    cls_name = value['__class__']
                    mod = import_module(f'models.{the_classes[cls_name]}')
                    Class = getattr(mod, cls_name)
                    self.new(Class(**value))
        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
