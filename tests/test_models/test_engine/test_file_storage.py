#!/usr/bin/env python3
"""
    Module to test: FileStorage class.
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models


class FileStorage_testing(unittest.TestCase):
    """ Test: FileStorage class."""
    __file_path = "file.json"

    def test_doc_module(self):
        """test: documentation for the module"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_doc_class(self):
        """test: documentation for the class FileStorage"""
        self.assertIsNotNone(FileStorage.__doc__)

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
        save_text = ""
        f = open("file.json", "r")
        ss = f.read();
        self.assertIn("BaseModel." + b.id, ss)

    def test_reload(self):
        """testing reload"""
        b = BaseModel()
        so = FileStorage()
        so.reload()
        self.assertIn("BaseModel." + b.id, so.all())


if __name__ == '__main__':
    unittest.main()
