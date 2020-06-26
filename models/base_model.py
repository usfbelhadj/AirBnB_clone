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
        return ("{}{}{}".format(type(self).__name__,self.id,self.__dict__))