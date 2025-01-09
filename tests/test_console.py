#!/usr/bin/python3
"""Test Console"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.state import State
from models.place import Place


class TestConsole(unittest.TestCase):
    """Test the HBNB console"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up test environment"""
        storage.all().clear()
        try:
            storage.save()
        except:
            pass

    def test_create_state(self):
        """Test create command with State"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="California"')
            state_id = f.getvalue().strip()
            
            # Verify state was created with correct name
            state = storage.all()["State." + state_id]
            self.assertEqual(state.name, "California")

    def test_create_place(self):
        """Test create command with Place and multiple parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = 'create Place city_id="0001" user_id="0001" ' \
                  'name="My_little_house" number_rooms=4 number_bathrooms=2 ' \
                  'max_guest=10 price_by_night=300 latitude=37.773972 ' \
                  'longitude=-122.431297'
            self.console.onecmd(cmd)
            place_id = f.getvalue().strip()
            
            # Verify place was created with correct attributes
            place = storage.all()["Place." + place_id]
            self.assertEqual(place.city_id, "0001")
            self.assertEqual(place.user_id, "0001")
            self.assertEqual(place.name, "My little house")
            self.assertEqual(place.number_rooms, 4)
            self.assertEqual(place.number_bathrooms, 2)
            self.assertEqual(place.max_guest, 10)
            self.assertEqual(place.price_by_night, 300)
            self.assertEqual(place.latitude, 37.773972)
            self.assertEqual(place.longitude, -122.431297)

    def test_create_invalid_syntax(self):
        """Test create command with invalid syntax"""
        with patch('sys.stdout', new=StringIO()) as f:
            # Missing class name
            self.console.onecmd('create')
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            # Invalid class name
            self.console.onecmd('create MyModel')
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_invalid_parameters(self):
        """Test create command with invalid parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            # Invalid parameter format should be skipped
            self.console.onecmd('create State name=California')  # Missing quotes
            state_id = f.getvalue().strip()
            state = storage.all()["State." + state_id]
            self.assertFalse(hasattr(state, 'name'))

    def test_parameter_types(self):
        """Test different parameter types"""
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = 'create Place name="Test_House" number_rooms=5 ' \
                  'latitude=37.77 price=100'
            self.console.onecmd(cmd)
            place_id = f.getvalue().strip()
            place = storage.all()["Place." + place_id]
            
            # Verify parameter types
            self.assertEqual(place.name, "Test House")  # String with space
            self.assertEqual(place.number_rooms, 5)     # Integer
            self.assertEqual(place.latitude, 37.77)     # Float