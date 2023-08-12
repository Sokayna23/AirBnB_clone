#!/usr/bin/python3
"""testing BaseModel"""
from models.place import Place
import unittest


class Place_Testing(unittest.TestCase):
    """
    testing place class
    """

    def test_1(self):
        """ testing if a unique id was generated"""
        b1 = Place()
        b2 = Place()
        self.assertNotEqual(b1.id, b2.id)
