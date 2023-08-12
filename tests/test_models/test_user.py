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

    def test_3(self):
        """
        testing password
        """
        u1 = User()
        self.assertEqual(u1.password, "")

    def test_4(self):
        """
        testing first_name
        """
        u1 = User()
        self.assertEqual(u1.first_name, "")

    def test_5(self):
        """
        testing last_name
        """
        u1 = User()
        self.assertEqual(u1.last_name, "")
