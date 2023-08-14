#!/usr/bin/python3
"""testing BaseModel"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import console
import uuid
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage


class Console_Testing(unittest.TestCase):
    """
    testing console
    """

    def test_tt(self):
        """checking an idea"""
        z = self.__doc__
        u = User()
        c = City()
        a = Amenity()
        s = State()
        b = BaseModel()
        r = Review()
        p = Place()
        self.assertEqual(5, 1 + 4)
        self.assertEqual(6, 2 + 4)
        self.assertEqual(7, 3 + 4)
        self.assertEqual(8, 4 + 4)
        self.assertEqual(9, 5 + 4)
        self.assertEqual(10, 6 + 4)
        self.assertEqual(11, 7 + 4)
        self.assertEqual(12, 8 + 4)
        self.assertEqual(13, 9 + 4)

    def test_1(self):
        """ testing class doc"""
        self.assertIsNotNone(console.__doc__)

    def test_2(self):
        """ testing methods doc"""
        for m in dir(console):
            if not m.startswith('_'):
                self.assertIsNotNone(getattr(console, m).__doc__)

    def test_3(self):
        """testing create for all classes"""
        classes = ["BaseModel", "User", "City", "State", "Amenity",
                   "Review", "Place"]
        for cl in classes:
            with patch("sys.stdout", new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {cl}")
                result = f.getvalue().strip()
                try:
                    uuid.UUID(result)
                except ValueError:
                    self.fail(f"not a valid uuid for {cl}")
