#!/usr/bin/python3
"""testing BaseModel"""
from models.review import Review
import unittest


class Review_Testing(unittest.TestCase):
    """
    testing Review class
    """

    def test_1(self):
        """ testing if a unique id was generated"""
        b1 = Review()
        b2 = Review()
        self.assertNotEqual(b1.id, b2.id)

    def test_2(self):
        """ testing if a unique id was generated"""
        b1 = Review()
        self.assertNotEqual(b1.place_id, "")
        self.assertNotEqual(b1.user_id, "")
        self.assertNotEqual(b1.text, "")
