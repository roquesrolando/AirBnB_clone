#!/usr/bin/python3
"""
contains FileStorage instance
"""
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.base_model import BaseModel
classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "Amenity": Amenity, "City": City, "Review": Review, "Place": Place}

try:
    from models.engine.file_storage import FileStorage
except:
    pass

storage = FileStorage()
storage.reload()
