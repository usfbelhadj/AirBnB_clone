#!/usr/bin/python3
"""Module for Base class for the AirBnB clone console."""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class for Base Model"""
    def __init__(self, *args, **kwargs):
        """init"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for arg in kwargs:
                if arg == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif arg == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[arg] = kwargs[arg]
        else:
            storage.new(self)

    def __str__(self):
        """str"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        """save"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to_dict"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
