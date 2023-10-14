#!/usr/bin/python3
"""
Module to test Place Class
"""

import unittest
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
import os


class TestState(unittest.TestCase):
    """Defines the testcases for Place"""

    def setUp(self):
        """Sets up test methods"""
        pass

    def resetStorage(self):
        """Resets data created by FileStorage"""
        storage = FileStorage()
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_place_inherits_from_base_model(self):
        """verifies that Place inherits from BaseModel"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_place_attribute_types(self):
        """checks place attributes"""
        place_attr = Place()
        self.assertEqual(type(place_attr.city_id), str)
        self.assertEqual(type(place_attr.user_id), str)
        self.assertEqual(type(place_attr.name), str)
        self.assertEqual(type(place_attr.description), str)
        self.assertEqual(type(place_attr.number_rooms), int)
        self.assertEqual(type(place_attr.number_bathrooms), int)
        self.assertEqual(type(place_attr.max_guest), int)
        self.assertEqual(type(place_attr.price_by_night), int)
        self.assertEqual(type(place_attr.latitude), float)
        self.assertEqual(type(place_attr.longitute), float)
        self.assertEqual(type(place_attr.amenity_ids), list)

    def test_place_instantiation(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_new_method_on_place(self):
        storage = FileStorage()
        place = Place()
        storage.new(place)
        all_objects = storage.all()
        self.assertIn("Place." + place.id, all_objects)

    def tearDown(self):
        """"Tears down test methods"""
        self.resetStorage()
        pass


if __name__ == "__main__":
    unittest.main()
