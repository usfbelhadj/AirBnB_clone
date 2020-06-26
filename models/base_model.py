#!/usr/bin/python3
"""Module for Base classfor the AirBnB clone console."""

import uuid
from datetime import datetime


class BaseModel:
    """Class for base model"""

    def __init__(self, *args, **kwargs):
        """init"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return ("{}{}{}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["class"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
