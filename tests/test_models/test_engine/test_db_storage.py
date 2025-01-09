#!/usr/bin/python3
"""Test DBStorage"""
import unittest
import MySQLdb
from models.engine.db_storage import DBStorage
from models.state import State
from models import storage
import os
from unittest.mock import patch
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                "Skip if not using db storage")
class TestDBStorage(unittest.TestCase):
    """Test cases for DBStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST', 'localhost'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        """Clean up test environment"""
        self.cursor.close()
        self.db.close()

    def test_state_creation(self):
        """Test creating a state in database"""
        # Get initial count
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Create new state
        state = State(name="California")
        storage.new(state)
        storage.save()

        # Get new count
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        # Verify count increased by 1
        self.assertEqual(new_count, initial_count + 1)

    def test_all_method(self):
        """Test all() method"""
        # Create test state
        state = State(name="Texas")
        storage.new(state)
        storage.save()

        # Get all states
        all_states = storage.all(State)
        
        # Verify state exists in results
        self.assertTrue(len(all_states) > 0)
        found = False
        for obj in all_states.values():
            if obj.name == "Texas":
                found = True
                break
        self.assertTrue(found)

    def test_delete_method(self):
        """Test delete() method"""
        # Create test state
        state = State(name="Florida")
        storage.new(state)
        storage.save()

        # Get initial count
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Delete state
        storage.delete(state)
        storage.save()

        # Get new count
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        # Verify count decreased by 1
        self.assertEqual(new_count, initial_count - 1)