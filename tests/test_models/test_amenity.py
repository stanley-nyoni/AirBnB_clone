#!/usr/bin/python3
"""Module - test_amenity
   Test cases for Amenity class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """Test cases for the amenity class"""

    def test_amenity_inherits_from_base_model(self):
        """Verify that amenity inherits from Base Model"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_creation(self):
        """checks if an instance of the Amenity class can be
        created successfully
        """
        amenity = Amenity()
        self.assertIsNotNone(amenity)

    def test_amenity_attributes_defaults(self):
        """verifies that the default attribute values of an Amenity
         instance are as expected.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_attributes_assignment(self):
        """Check if you can  assign values to attributes
        of an Amenity instance.
        """
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_amenity_id_is_a_string(self):
        """Check if the  id of amenity is a string"""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)

    def test_new_method_amenity(self):
        """Verify that the amenity has been
        saved to the storage
        """
        storage = FileStorage()
        amenity = Amenity()
        storage.new(amenity)
        all_objects = storage.all()
        self.assertIn("Amenity." + amenity.id, all_objects)


if __name__ == '__main__':
    unittest.main()
