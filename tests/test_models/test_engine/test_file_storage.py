#!/usr/bin/python3
"""Test FileStorage"""
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models import storage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                "Skip if using db storage")
class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        try:
            os.rename("file.json", "tmp")
        except:
            pass
        self.storage = FileStorage()

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

    def test_all_method(self):
        """Test all() method"""
        # Test empty storage
        self.assertEqual(len(self.storage.all()), 0)

        # Add an object
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()

        # Test storage with object
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn("State." + state.id, self.storage.all())

    def test_new_method(self):
        """Test new() method"""
        state = State(name="Texas")
        self.storage.new(state)
        self.assertIn("State." + state.id, self.storage.all())

    def test_save_method(self):
        """Test save() method"""
        state = State(name="Florida")
        self.storage.new(state)
        self.storage.save()

        # Check if file exists
        self.assertTrue(os.path.exists("file.json"))

        # Check file contents
        with open("file.json", "r") as f:
            data = json.load(f)
            self.assertIn("State." + state.id, data)

    def test_reload_method(self):
        """Test reload() method"""
        state = State(name="New York")
        self.storage.new(state)
        self.storage.save()
        self.storage.all().clear()
        self.storage.reload()
        self.assertIn("State." + state.id, self.storage.all())

    def test_delete_method(self):
        """Test delete() method"""
        state = State(name="Oregon")
        self.storage.new(state)
        self.storage.save()
        self.storage.delete(state)
        self.assertNotIn("State." + state.id, self.storage.all())