#!/usr/bin/python3
"""Module that has test cases for the user
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """A test case for the User
    """

    def test_instantiation(self):
        """Tests instatiation of User class"""

        u = User()
        self.assertEqual(str(type(u)), "<class 'models.user.User'>")
        self.assertIsInstance(u, User)
        self.assertTrue(issubclass(type(u), BaseModel))

    def test_attr_are_class_attrs(self):
        """checks if attributes are of the class attributes."""

        u = User()
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))

    def test_attributes(self):

        u = User()
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")
        self.assertIs(type(u.email), str)
        self.assertIs(type(u.password), str)


if __name__ == '__main__':
    unittest.main()
