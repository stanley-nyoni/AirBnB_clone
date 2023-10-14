#!/usr/bin/python3
""" Module - test_user
    Test cases for User class
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Defines the test cases for user"""

    def test_user_inherits_from_base_model(self):
        """Verify that user inherits from base model"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_user_default_attributes(self):
        """Verify the default attributes"""

        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes_assignement(self):
        """verify the assignement of user attributes"""
        user1 = User()
        user1.email = "mqelisinyoni77@gmail.com"
        user1.password = "stan77"
        user1.first_name = "mqelisi"
        user1.last_name = "nyoni"

        self.assertEqual(user1.email, "mqelisinyoni77@gmail.com")
        self.assertEqual(user1.password, "stan77")
        self.assertEqual(user1.first_name, "mqelisi")
        self.assertEqual(user1.last_name, "nyoni")


if __name__ == '__main__':
    unittest.main()
