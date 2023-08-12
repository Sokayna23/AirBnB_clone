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
