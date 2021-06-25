#!/usr/bin/python3
"""

"""
from datetime import datetime
import uuid
import models

class BaseModel():
    """

    """
    def __init__(self, *args, **kwargs):
        """

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

        """
        return ("[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__))

    def save(self):
        """

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """

        """
        dictionary = dict(self.__dict__)

        dictionary["__class__"] = __class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
