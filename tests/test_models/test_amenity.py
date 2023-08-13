#!/usr/bin/python3
"""testing BaseModel"""
from models.amenity import Amenity
import unittest
import models


class Amenity_Testing(unittest.TestCase):
    """
    testing Aminity
    """

    def test_1(self):
        """ testing if a unique id was generated"""
        b1 = Amenity()
        b2 = Amenity()
        self.assertNotEqual(b1.id, b2.id)

    def test_2(self):
        """
        testing email
        """
        u1 = Amenity()
        self.assertEqual(u1.name, "")
        self.assertTrue(isinstance(u1.name, str))
        self.assertTrue(hasattr(u1, "name"))
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(models.amenity.__doc__)
