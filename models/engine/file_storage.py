#!/usr/bin/python3
"""Module for FileStorage class for the AirBnB clone console."""
import json
import datetime

class FileStorage:
    """Class for file Storage"""
    __file_path = file.json
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        FileStorage.__objects = self.obj