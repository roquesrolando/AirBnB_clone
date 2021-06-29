#!/usr/bin/python3
"""
contains FileStorage instance
"""
from models.user import User
from models.base_model import BaseModel
classes = {"BaseModel": BaseModel, "User": User}

try:
    from models.engine.file_storage import FileStorage
except:
    pass

storage = FileStorage()
storage.reload()
