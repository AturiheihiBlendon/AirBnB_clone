#!/usr/bin/python3
"""A module containing test cases for BaseModel
"""

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test case for the BaseModel class
    """
    def test_datetime_created_at(self):
        """Tests if created_at is a datetime obj."""

        b = BaseModel()
        self.assertTrue(type(b.created_at) is datetime)

    def test_datetime_updated_at(self):
        """Tests if updated_at is a datetime obj."""

        b = BaseModel()
        self.assertTrue(type(b.updated_at) is datetime)

    def test_unique_id(self):
        """Checks if instances have unique ids."""

        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_id(self):
        """Checks for id"""

        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))

    def test_save_initial(self):
        """Tests the public instance method save() updates the updated_at."""

        b = BaseModel()
        self.assertIs(b.created_at, b.updated_at)

    def test_save(self):
        """Tests the public instance method save() updates the updated_at."""

        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_str(self):
        """Test for __str__ representation."""

        b = BaseModel()
        self.assertEqual(str(b),
                         "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_to_dict(self):
        """Tests for __dict__ public instance."""

        b = BaseModel()
        d = datetime.now()
        b.id = "12345"
        b.created_at = b.updated_at = d
        test_dict = {
            "id": "12345",
            "created_at": d.isoformat(),
            "updated_at": d.isoformat(),
            "__class__": "BaseModel"
            }
        self.assertDictEqual(test_dict, b.to_dict())


if __name__ == '__main__':
    unittest.main()
