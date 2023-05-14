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

    def test_to_dict(self):
        """test to_dict()."""

        c = BaseModel()
        c.name = "Steve"
        c.age = 26
        d = c.to_dict()
        self.assertEqual(d["id"], c.id)
        self.assertEqual(d["__class__"], type(c).__name__)
        self.assertEqual(d["created_at"], c.created_at.isoformat())
        self.assertEqual(d["updated_at"], c.updated_at.isoformat())
        self.assertEqual(d["name"], c.name)
        self.assertEqual(d["age"], c.age)


if __name__ == '__main__':
    unittest.main()
