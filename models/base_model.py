#!/usr/bin/python3
"""Module for Base classfor the AirBnB clone console."""

import uuid
import datetime

class BaseModel:
    """Class for base model"""
    
    def __init__(self, *args, **kwargs):
        """init"""
        if kwargs is not None and args is not None:
            for i in kwargs:
                if "created_at" in i:
                    
        self.id = str(uuid.uuid4())
    
    