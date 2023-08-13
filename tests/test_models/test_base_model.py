#!/usr/bin/python3
"""testing BaseModel"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep


class BaseModel_Testing(unittest.TestCase):
    """test for BaseModel """

    def test_1(self):
        """ testing if a unique id was generated"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_2(self):
        """ test: save method"""
        b1 = BaseModel()
        up1 = b1.updated_at.isoformat()
        sleep(2)
        b1.save()
        up2 = b1.updated_at.isoformat()
        self.assertNotEqual(up2, up1)

    def test_3(self):
        """ test: type of attributes"""
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(type(b1.updated_at), datetime)

    def test_4(self):
        """ test: type of attributes"""
        try:
            b1 = BaseModel
            a = b1.id
            self.fail("BaseModel is not a class")
        except AttributeError:
            pass
