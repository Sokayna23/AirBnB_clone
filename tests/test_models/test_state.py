#!/usr/bin/python3
"""testing BaseModel"""
from models.state import State
import unittest


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
        self.assertNotEqual(b1.name, "")
