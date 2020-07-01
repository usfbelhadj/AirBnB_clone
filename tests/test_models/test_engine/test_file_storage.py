#!/usr/bin/python3
"""Test FileStorage"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test FileStorage"""

    def test_storage(self):
        """Test storage"""
        self.assertIsInstance(storage, FileStorage)
