#!/usr/bin/python3
"""Test BaseModel"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test environment"""
        self.base = BaseModel()
        try:
            os.rename("file.json", "tmp")
        except:
            pass

    def tearDown(self):
        """Clean up test environment"""
        try:
            os.remove("file.json")
        except:
            pass
        try:
            os.rename("tmp", "file.json")
        except:
            pass

    def test_init(self):
        """Test initialization"""
        self.assertIsInstance(self.base, BaseModel)
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))

    def test_save(self):
        """Test save method"""
        old_updated = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated, self.base.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_dict["created_at"], str)
        self.assertIsInstance(base_dict["updated_at"], str)

    def test_str(self):
        """Test string representation"""
        string = str(self.base)
        self.assertIsInstance(string, str)
        self.assertIn("BaseModel", string)
        self.assertIn(self.base.id, string)