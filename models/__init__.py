#!/usr/bin/python3
"""
contains FileStorage instance
"""
from models.base_model import BaseModel
classes = {"BaseModel": BaseModel}
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
