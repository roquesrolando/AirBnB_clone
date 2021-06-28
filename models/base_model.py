#!/usr/bin/python3
"""
This module contains the BaseModel class for all instances
"""
from datetime import datetime
import uuid
import models

class BaseModel():
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialies BaseModel attributes
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String of a class
        """
        return ("[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Saves an object to a JSON file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary with key and values of __dict__
        """
        dictionary = dict(self.__dict__)

        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
