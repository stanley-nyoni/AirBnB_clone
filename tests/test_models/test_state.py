#!/usr/bin/python3
"""
Module to test State Class
"""

import unittest
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
import os

class TestState(unittest.TestCase):
    """Defines the testcases for State"""

    def setUp(self):
        """Sets up test methods"""
        pass

    def resetStorage(self):
        """Resets data created by FileStorage"""
        storage = FileStorage()
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_state_inherits_from_base_model(self):
        """verifies that state inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_state_name(self):
        """checks if the default name is an empty string"""
        state_instance = State()
        self.assertEqual(state_instance.name, "")

    def test_new_method_on_state(self):
        storage = FileStorage()
        state = State()
        storage.new(state)
        all_objects = storage.all()
        self.assertIn("State." + state.id, all_objects)

    def tearDown(self):
        """"Tears down test methods"""
        self.resetStorage()
        pass

if __name__ == "__main__":
    unittest.main()
