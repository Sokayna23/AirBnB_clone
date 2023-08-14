#!/usr/bin/env python3
"""
    Module to test: FileStorage class.
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import models
import os


class FileStorage_testing(unittest.TestCase):
    """ Test: FileStorage class."""
    __file_path = "file.json"

    def test_doc_module(self):
        """test: documentation for the module"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_doc_class(self):
        """test: documentation for the class FileStorage"""
        for m in dir(FileStorage):
            if not m.startswith('_'):
                self.assertIsNotNone(getattr(FileStorage, m).__doc__)

    def test_all(self):
        """test: all() method."""
        b = BaseModel()
        objects = models.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """test: new() method."""
        b = BaseModel()
        key_name = "BaseModel."+b.id
        self.assertIsInstance(models.storage.all()[key_name], BaseModel)
        self.assertEqual(models.storage.all()[key_name], b)
        self.assertIn(key_name, models.storage.all())
        self.assertTrue(models.storage.all()[key_name] is b)

    def test_save(self):
        """testing save"""
        b = BaseModel()
        models.storage.new(b)
        models.storage.save()
        ss = ""
        with open("file.json", "r") as f:
            ss = f.read()
        self.assertIn("BaseModel." + b.id, ss)

    def test_reload_user(self):
        """testing reload"""
        b = User()
        so = FileStorage()
        so.reload()
        self.assertIn("User." + b.id, so.all())

    def test_reload_all(self):
        """testing reload"""
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review}
        for k, v in classes.items():
            b = v()
            so = FileStorage()
            so.reload()
            self.assertIn(f"{k}." + b.id, so.all())

    def test_attributes(self):
        """test attributes"""
        os.remove("file.json")
        f_s = FileStorage()
        # self.assertTrue(hasattr(f_s, "__file_path"))
        # self.assertTrue(hasattr(f_s, "__objects"))
        lo = len(f_s.all())
        b = BaseModel()
        f_s.reload()
        self.assertEqual(len(f_s.all()), lo + 1)


if __name__ == '__main__':
    unittest.main()
