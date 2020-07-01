#!/usr/bin/python3
"""test BaseModel"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests BaseBodel"""

    def test_instances(self):
        """Tests instances"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_id(self):
        """Test id"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_str(self):
        """
            Test __str__ method
        """
        bm = BaseModel()
        self.assertEqual(type(bm.__str__()), str)

    def test_str_format(self):
        """Test str format"""
        instance = BaseModel()
        s = instance.__str__()
        _format = "[{}] ({}) {}".\
            format(bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(s, _format)

    def test_kwargs(self):
        """Test kwargs"""
        kwargs = {"name": "Betty"}
        instance = BaseModel(**kwargs)
        self.assertEqual(instance.name, "Betty")
