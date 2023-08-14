#!/usr/bin/python3
"""
Unittest for amenity.py
"""


import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class
    """
    def setUp(self):
        """
        Setup instance
        """
        self.amenity = Amenity()

    def test_instance(self):
        """
        Checks if instance is of Amenity class
        """
        self.assertIsInstance(self.amenity, Amenity)

    def test_name_attr(self):
        """
        Checks if amenity has attribute name and is empty
        """
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_id_attr(self):
        """
        Checks if amenity has attribute id and is empty
        """
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertEqual(self.amenity.id, "")

    def test_created_at_attr(self):
        """
        Checks if amenity has attribute created_at and is datetime
        """
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(type(self.amenity.created_at) is datetime.datetime)

    def test_updated_at_attr(self):
        """
        Checks if amenity has attribute updated_at and is datetime
        """
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(type(self.amenity.updated_at) is datetime.datetime)

    def test_str(self):
        """
        Checks if print(self.amenity) is string
        """
        self.assertTrue(type(self.amenity.__str__()) is str)

    def test_save(self):
        """
        Checks if save updates the attribute updated_at
        """
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_to_dict(self):
        """
        Checks if to_dict returns the correct dictionary
        """
        self.assertEqual("to_dict" in dir(self.amenity), True)
