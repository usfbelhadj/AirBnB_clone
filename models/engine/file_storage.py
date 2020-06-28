#!/usr/bin/python3
"""Module for FileStorage class for the AirBnB clone console."""
import json
from os import path
class FileStorage:
    """Class for file Storage"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        FileStorage.__objects[type(obj).__name__ +"."+obj.id] = obj
    def save(self):
        '''save: to json'''
        dct = {}
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            for k, v in FileStorage.__objects.items():
                dct[k] = v.to_dict()
            return json.dumps(dct, f)
    
    def reload(self):
        from models.base_model import BaseModel
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj = json.load(f)
                except:
                    return
                dct = {}
                for key in obj.keys():
                    dct[key] = BaseModel(**obj.get(key))
                FileStorage.__objects = dct
        else:
            return