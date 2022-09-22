#!/usr/bin/python3
"""A module with the City test cases
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test case for the City class
    """

    def test_instatiation(self):
        """Test if object is instatiated
        """

        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")
        self.assertIsInstance(city, City)
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_attr_are_class_attrs(self):
        """checks if attributes are of the class attributes."""

        city = City()
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "state_id"))

    def test_attributes(self):

        city = City()
        self.assertTrue(city.name == "")
        self.assertTrue(city.state_id == "")


if __name__ == '__main__':
    unittest.main()
