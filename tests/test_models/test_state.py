#!/usr/bin/python3
"""testing BaseModel"""
from models.state import State
import unittest
import models


class State_Testing(unittest.TestCase):
    """
    testing state class
    """

    def test_1(self):
        """ testing if a unique id was generated"""
        b1 = State()
        b2 = State()
        self.assertNotEqual(b1.id, b2.id)

    def test_2(self):
        """ testing if a unique id was generated"""
        b1 = State()
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(models.state.__doc__)

        self.assertEqual(b1.name, "")
        self.assertTrue(isinstance(b1.name, str))
        self.assertTrue(hasattr(b1, "name"))
