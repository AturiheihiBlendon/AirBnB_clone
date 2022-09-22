#!/usr/bin/python3
"""A module that has test cases for the Place class
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class
    """

    def test_instatiation(self):
        """Test if the object is instatiated
        """

        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_attr_are_class_attrs(self):
        """checks if attributes are of the class attributes."""

        place = Place()
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_attributes(self):

        place = Place()
        self.assertTrue(place.city_id == "")
        self.assertTrue(place.user_id == "")
        self.assertTrue(place.name == "")
        self.assertTrue(place.description == "")
        self.assertTrue(place.number_rooms == 0)
        self.assertTrue(place.number_bathrooms == 0)
        self.assertTrue(place.max_guest == 0)
        self.assertTrue(place.latitude == 0.0)
        self.assertTrue(place.longitude == 0.0)
        self.assertTrue(place.amenity_ids == [])


if __name__ == '__main__':
    unittest.main()
