#!/usr/bin/python3

"""
Module - test_base_model
Test cases for base model
"""


import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        pass

    def test_creation_and_initialization(self):
        """Check if attributes are correctly initialized"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_str_method(self):
        """Check the returned string, if matches the expected"""

        base = BaseModel()
        self.assertEqual(str(base), "[BaseModel] ({}) {}".format(base.id, base.__dict__))

    def test_save(self):
        """Check if we successfully updated the updated_at attribute"""

        base = BaseModel()
        initial_update = base.updated_at
        # Update time by calling save()
        base.save()
        recent_update = base.updated_at
        # Recent update should be always greater than initial update
        self.assertTrue(recent_update > initial_update)

    def test_to_dict(self):
        """Check the dictionary represantion of an instance"""

        base = BaseModel()
        base_dict = base.to_dict()
        self.assertTrue('id' in base_dict)
        self.assertTrue('created_at' in base_dict)
        self.assertTrue('updated_at' in base_dict)
        self.assertTrue('__class__' in base_dict)

    def test_to_dict_value_types(self):
        """Check the values of dict if theyre of expected type"""

        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict['id'], str)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertEqual(base_dict['__class__'], 'BaseModel')

    def tearDown(self):
        pass
    
if __name__ == '__main__':
    unittest.main()