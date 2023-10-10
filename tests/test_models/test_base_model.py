#!/usr/bin/python3

"""
Module - test_base_model
Test cases for base model
"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_creation_and_initialization(self):
        base = BaseModel()
        self.assertIsInstance(base.id, str)


if __name__ == '__main__':
    unittest.main()