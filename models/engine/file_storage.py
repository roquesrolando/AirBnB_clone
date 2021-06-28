#!/usr/bin/python3
"""
Manage file storage for BaseModel
"""
import json
from .. import classes

class FileStorage:
    """
    Serielizes and deserialize to a JSON file and from a JSON file
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary """
        return self.__objects

    def new(self, obj):
        """ Add to dictionary """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Serializes objects JSON file """
        new_dic = {}
        with open(self.__file_path, mode='w', encoding='UTF-8') as a_dict:
            for key, value in self.__objects.items():
                new_dic[key] = value.to_dict()
            json.dump(new_dic, a_dict)

    def reload(self):
        """
        Deserialies from JSON file
        """
        try:
            filename = self.__file_path
            with open(filename, mode='r', encoding='UTF-8') as a_dict:
                b_dict = json.load(a_dict)
            for key in b_dict:
                self.__objects[key] = classes[b_dict[key]["__class__"]](**b_dict[key])
        except FileNotFoundError:
            pass
