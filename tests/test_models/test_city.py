#!/usr/bin/python3
"""testing BaseModel"""
from models.city import City
import unittest


class City_Testing(unittest.TestCase):
    """
    testing city class
    """

    def test_1(self):
        """ testing if a unique id was generated"""
        b1 = City()
        b2 = City()
        self.assertNotEqual(b1.id, b2.id)

    def test_2(self):
        """
        testing name
        """
        u1 = City()
        self.assertEqual(u1.name, "")

    def test_3(self):
        """
        testing state_id
        """
        u1 = City()
        self.assertEqual(u1.state_id, "")
