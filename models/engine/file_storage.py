#!/usr/bin/python3
"""This module contains the FileStorage class"""
import json


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
                the_classes = {'BaseModel': "base_model", 'User': "user"}
                for value in data.values():
                    cls_name = value['__class__']
                    mod = import_module(f'models.{the_classes[cls_name]}')
                    Class = getattr(mod, cls_name)
                    self.new(Class(**value))
        except FileNotFoundError:
            pass
