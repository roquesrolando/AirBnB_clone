#!/usr/bin/python3
"""
Manage file storage for BaseModel objects
"""
from models.base_model import BaseModel
import json

class FileStorage():
    """
    Serielizes and deserialiez to a JSON file and from a JSOn file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Adds to dictionary
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes objects to JSOn file
        """
        a_dict = {}

        with open(self.__file_path, 'a') as a_file:
            for key, value in self.__objects.items():
                a_dict[key] = value.to_dict()
            json.dump(a_dict, a_file)

    def reload(self):
        """
        Deserialies from JSON file
        """
        try:
            with open(self.__file_path, 'r') as a_file:
                b_dict = json.load(a_file)
                for key, value in b_dict.items():
                    b_dict[key] = value
        except FileNotFoundError:
            pass

