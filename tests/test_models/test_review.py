#!/usr/bin/python3
"""testing BaseModel"""
from models.review import Review
import unittest
import models


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
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(models.review.__doc__)

        self.assertEqual(b1.place_id, "")
        self.assertEqual(b1.user_id, "")
        self.assertEqual(b1.text, "")
        self.assertTrue(isinstance(b1.place_id, str))
        self.assertTrue(isinstance(b1.user_id, str))
        self.assertTrue(isinstance(b1.text, str))

        self.assertTrue(hasattr(b1, "place_id"))
        self.assertTrue(hasattr(b1, "user_id"))
        self.assertTrue(hasattr(b1, "text"))
