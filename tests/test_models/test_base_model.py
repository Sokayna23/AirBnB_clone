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
        b2 = BaseModel(b1.to_dict())
        self.assertEqual(b1.id, b2.id)

    def test_3(self):
        """ test: creating object from another"""
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(type(b1.updated_at), datetime)

    def test_save(self):
        """Test for save() method"""
        b = BaseModel()
        with self.assertRaises(TypeError) as error:
            b.save("exess")
        self.assertEqual(str(error.exception), 'BaseModel.save() takes 1'
                         + ' positional argument but 2 were given')

        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

     def test_to_dict(self):
        """Tests the to_dict() function of a BaseModel instance"""
        base = BaseModel()
        self.assertIsInstance(base.to_dict(), dict)

        base_dict = base.__dict__.copy()
        base_dict['__class__'] = base.__class__.__name__
        base_dict['created_at'] = (base.created_at
                                   .strftime('%Y-%m-%dT%H:%M:%S.%f'))
        base_dict['updated_at'] = (base.updated_at
                                   .strftime('%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(base.to_dict(), base_dict)

        self.assertEqual(len(base.to_dict()), len(base_dict))

        for key, value in base.to_dict().items():
            self.assertEqual(base_dict[key], value)

        base.name = "My instance name"
        base_dict['name'] = "My instance name"
        self.assertEqual(base.to_dict(), base_dict)

    def test_str(self):
        """Tests the __str__() function return of a BaseModel instance"""
        base = BaseModel()
        self.assertIsInstance(str(base), str)

        expected = f'[{base.__class__.__name__}] ({base.id}) {base.__dict__}'
        self.assertEqual(str(base), expected)

        base.name = "My instance name"
        expected = f'[{base.__class__.__name__}] ({base.id}) {base.__dict__}'
        self.assertEqual(str(base), expected)

