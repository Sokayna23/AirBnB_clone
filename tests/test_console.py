#!/usr/bin/python3
"""testing BaseModel"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import console
import uuid

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
    
    def test_3(self):
        """testing validty of uuid for all classes"""
        classes = ["BaseModel","User","City","State","Amenity",
                   "Review","Place"]
        for cl in classes:
            with patch("sys.stdout", new=StringIO()) as f:
                        HBNBCommand().onecmd(f"create {cl}")
                        result = f.getvalue().strip()
                        try:
                            uuid.UUID(result)
                        except ValueError:
                            self.fail(f"not a valid uuid for {cl}")
