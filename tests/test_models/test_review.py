#!/usr/bin/python3
"""
Module to test Review Class
"""

import unittest
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
import os

class TestState(unittest.TestCase):
    """Defines the testcases for Review"""

    def setUp(self):
        """Sets up test methods"""
        pass

    def resetStorage(self):
        """Resets data created by FileStorage"""
        storage = FileStorage()
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_review_inherits_from_base_model(self):
        """verifies that review inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_review_attribute_types(self):
        """checks if the default name is an empty string"""
        review_attr = Review()
        self.assertEqual(type(review_attr.place_id), str)
        self.assertEqual(type(review_attr.user_id), str)
        self.assertEqual(type(review_attr.text), str)

    def test_review_instantiation(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_new_method_on_review(self):
        storage = FileStorage()
        review = Review()
        storage.new(review)
        all_objects = storage.all()
        self.assertIn("Review." + review.id, all_objects)

    def tearDown(self):
        """"Tears down test methods"""
        self.resetStorage()
        pass

if __name__ == "__main__":
    unittest.main()
                   

