#!/usr/bin/python3
"""Module for FileStorage class for the AirBnB clone console."""
import json
from os import path
from models.base_model import BaseModel

class FileStorage:
    """Class for file Storage"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        FileStorage.__objects[type(obj).__name__ +"."+obj.id] = obj
        self.obj = type(self).__name__
        FileStorage.__objects = self.obj
    def save(self):
        '''save: to json'''
        with open(__file_path, 'w', encoding='utf-8') as f:
            return f.write(json.dumps(__objects))
    def reload(self):
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj = json.load(f)
                dct = {}
                for key in obj.keys():
                    dct[key] = BaseModel(**obj.get(key))
                FileStorage.__objects = dct
        else:
            return