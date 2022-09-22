#!/usr/bin/python3
"""A module having test cases for the Review class
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test case for the Review class
    """

    def test_instatiation(self):
        """Test if the obj is instatiated
        """
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_attr_are_class_attrs(self):
        """checks if attributes are of the class attributes."""

        city = Review()
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_attributes(self):

        city = Review()
        self.assertTrue(city.place_id == "")
        self.assertTrue(city.user_id == "")
        self.assertTrue(city.text == "")


if __name__ == '__main__':
    unittest.main()
