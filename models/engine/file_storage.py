#!/usr/bin/python3
"""

"""
from models.base_model import BaseModel
import json

class FileStorage():
    """

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """

        """
        return self.__objects

    def new(self, obj):
        """

        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """

        """
        a_dict = {}

        with open(self.__file_path, 'a') as a_file:
            for key, value in self.__objects.items():
                a_dict[key] = value.to_dict()
            json.dump(a_dict, a_file)

    def reload(self):
        """

        """
        a_dict = {}

        try:
            with open(self.__file_path) as a_file:
                for line in a_file:
                    a_dict = json.load(line)

            for key, value in a_dict.items():
                BaseModel.__dict__[key] = value

        except:
            pass

