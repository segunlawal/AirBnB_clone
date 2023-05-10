#!/usr/bin/python3
"""This module defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """This class defines a base model"""
    def __init__(self):
        """Initialization method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary of the object instance"""
        dict_obj = self.__dict__.copy()
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        dict_obj["__class__"] = self.__class__.__name__
        return dict_obj