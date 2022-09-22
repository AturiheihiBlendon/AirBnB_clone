#!/usr/bin/python3
"""A module that has test cases for the State class
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test case for the State class
    """

    def test_instatiation(self):
        """Test if object is instatiated
        """
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_attr_are_class_attrs(self):
        """checks if attributes are of the class attributes."""

        city = State()
        self.assertTrue(hasattr(State, "name"))
    
    def test_attributes(self):

        city = State()
        self.assertTrue(city.name == "")


if __name__ == '__main__':
    unittest.main()
