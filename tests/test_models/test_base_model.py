#!/usr/bin/python3

"""
Module - test_base_model
Test cases for base model
"""

import os
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        pass

    def test_creation_and_initialization(self):
        """Check if attributes are correctly initialized"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_init_with_no_args(self):
        """"Tests __init__ with no arguments passed to it"""
        with self.assertRaises(TypeError) as error:
            BaseModel.__init__()
        errmsg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), errmsg)

    def test_init_with_multiple_args(self):
        """"Tests __init__ with multiple arguments passed to it"""
        a = [i for i in range(100)]
        bm = BaseModel(0, 1, 2, 3, 4, 5)
        bm = BaseModel(*a)

    def test_str_method(self):
        """Check the returned string, if matches the expected"""

        base = BaseModel()
        self.assertEqual(str(base), "[BaseModel] ({}) {}".format(
                                                    base.id, base.__dict__))

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

    def test_creating_an_instance_from_dict(self):
        """Creating an instance from a dictionary"""
        # Get the dictionary ready
        data = {
            'id': 'my_id',
            'created_at': '2023-10-11T10:00:00.000000',
            'updated_at': '2023-10-11T11:00:00.000000',
            'name': 'My Base',
            'number': 234,
            '__class__': 'BaseModel'
        }
        # Create an object using **data
        obj = BaseModel(**data)

        self.assertEqual(obj.id, 'my_id')
        self.assertEqual(obj.name, 'My Base')
        self.assertEqual(obj.number, 234)

        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
