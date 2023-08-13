#!/usr/bin/python3
"""testing BaseModel"""
import unittest
import console


class Console_Testing(unittest.TestCase):
    """
    testing console
    """

    def test_1(self):
        """ testing class doc"""
        self.assertIsNotNone(console.__doc__)

    def test_2(self):
        """ testing methods doc"""
        for m in dir(console) :
            if not m.startswith('_'):
                self.assertIsNotNone(getattr(console, m).__doc__)
