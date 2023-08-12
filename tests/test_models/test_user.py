#!/usr/bin/python3
"""
testing BaseModel
"""
from models.user import User
import unittest


class User_Testing(unittest.TestCase):
    """
    testing user class
    """

    def test_1(self):
        """
        testing if a unique id was generated
        """
        b1 = User()
        b2 = User()
        self.assertNotEqual(b1.id, b2.id)

    def test_2(self):
        """
        testing email
        """
        u1 = User()
        self.assertEqual(u1.email, "")
        self.assertEqual(u1.password, "")
        self.assertEqual(u1.first_name, "")
        self.assertEqual(u1.last_name, "")
