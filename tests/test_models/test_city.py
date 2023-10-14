#!/usr/bin/python3
"""Module - test_city
   Test cases for City class
"""

import unittest
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """Test cases for the city class"""

    def test_city_inherits_from_base_model(self):
        """Verifyb that city inherits from Base Model"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_city_has_attributes(self):
        """Verify that city has attributes"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "created_at"))

    def test_city_attributes_types(self):
        """Verify the type of city attributes"""

        city = City()
        self.assertEqual(type(city.name), str)
        self.assertEqual(type(city.state_id), str)

    def test_new_method(self):
        """Verify that the city has been saved to the storage"""
        storage = FileStorage()
        city = City()
        storage.new(city)
        all_objects = storage.all()
        self.assertIn("City." + city.id, all_objects)


if __name__ == '__main__':
    unittest.main()
