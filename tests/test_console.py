#!/usr/bin/python3
"""testing BaseModel"""
from models.base_model import BaseModel
import unittest
import console

class Console_Testing(unittest.TestCase):
    """
    testing console
    """

    def test_1(self):
        """ testing if a unique id was generated"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
