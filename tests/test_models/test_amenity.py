#!/usr/bin/python3
"""A module that has test cases for the Amenity class
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestState(unittest.TestCase):
    """Test case for the Amenity class
    """

    def test_instatiation(self):
        """Test if object is instatiated
        """
        amenity = Amenity()
        self.assertEqual(str(type(amenity)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_attr_are_class_attrs(self):
        """checks if attributes are of the class attributes."""

        amenity = Amenity()
        self.assertTrue(hasattr(Amenity, "name"))

    def test_attributes(self):

        amenity = Amenity()
        self.assertTrue(amenity.name == "")


if __name__ == '__main__':
    unittest.main()
