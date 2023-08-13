#!/usr/bin/python3
"""testing BaseModel"""
from models.base_model import BaseModel
import unittest
from datetime import datetime


class BaseModel_Testing(unittest.TestCase):
    """test for BaseModel """

    def test_1(self):
        """ testing if a unique id was generated"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_2(self):
        """ test: creating object from another"""
        b1 = BaseModel()
        b2 = BaseModel(**b1.to_dict())
        self.assertEqual(b1.id, b2.id)

    def test_3(self):
        """ test: creating object from another"""
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(type(b1.updated_at), datetime)
