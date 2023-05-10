#!/usr/bin/python3
"""This module contains the TestBaseModel class"""
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """unit test cases for BaseModel class"""
    def test_id_is_string(self):
        """test if id is a string"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)

    def test_id_unique(self):
        """test whether id is unique"""
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_created_at_is_datetime(self):
        """test if created_at is a datetime object"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """test if updated_at is a datetime object"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime)
 
if __name__ == '__main__':
    unittest.main()
