#!/usr/bin/python3
"""Tests for FileStorage class"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    def setUp(self):
        """Set up test dependencies"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.e = f'{self.model.__class__.__name__}.{self.model.id}'

    def test_all(self):
        """test all() method"""
        self.storage.new(self.model)
        result = self.storage.all()
        self.assertIsInstance(result, dict)
        self.assertIn(self.e, result)
