#!/usr/bin/python3
"""Module for FileStorage class for the AirBnB clone console."""


import json
from os import path, stat


class FileStorage:
    """Class for file Storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All"""
        return FileStorage.__objects

    def new(self, obj):
        """New"""
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        '''save: to json'''
        _dict = {}
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            for key, val in FileStorage.__objects.items():
                _dict[key] = val.to_dict()
            json.dump(_dict, f)

    def reload(self):
        from models.base_model import BaseModel
        if path.isfile(FileStorage.__file_path) and not stat(FileStorage.__file_path).st_size == 0:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj = json.load(f)
                _dict = {}
                for key, val in obj.items():
                    _dict[key] = BaseModel(**val)
                FileStorage.__objects = _dict
        else:
            return