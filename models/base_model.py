#!/usr/bin/python3
"""
This module contains the BaseModel class for all instances
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        Initializer BaseModel attributes
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            del kwargs['__class__']
            kwargs["created_at"] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        String of a class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Saves an object to JSON file """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary with key and values of __dict__
        """
        todic = self.__dict__.copy()
        todic["__class__"] = self.__class__.__name__
        todic["created_at"] = self.created_at.isoformat()
        todic["updated_at"] = self.updated_at.isoformat()
        return todic
