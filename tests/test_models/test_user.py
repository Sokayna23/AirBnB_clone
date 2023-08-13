#!/usr/bin/python3
"""
testing BaseModel
"""
from models.user import User
import unittest
import models


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
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(models.user.__doc__)

        self.assertEqual(u1.email, "")
        self.assertEqual(u1.password, "")
        self.assertEqual(u1.first_name, "")
        self.assertEqual(u1.last_name, "")

        self.assertTrue(isinstance(u1.email, str))
        self.assertTrue(isinstance(u1.password, str))
        self.assertTrue(isinstance(u1.first_name, str))
        self.assertTrue(isinstance(u1.last_name, str))

        self.assertTrue(hasattr(u1, "email"))
        self.assertTrue(hasattr(u1, "password"))
        self.assertTrue(hasattr(u1, "first_name"))
        self.assertTrue(hasattr(u1, "last_name"))
