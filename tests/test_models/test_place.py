#!/usr/bin/python3
"""testing BaseModel"""
from models.place import Place
import unittest
import models


class Place_Testing(unittest.TestCase):
    """
    testing place class
    """

    def test_1(self):
        """ testing if a unique id was generated"""
        b1 = Place()
        b2 = Place()
        self.assertNotEqual(b1.id, b2.id)

    def test_2(self):
        """ testing attributes"""
        b1 = Place()
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(models.place.__doc__)

        self.assertEqual(b1.city_id, "")
        self.assertEqual(b1.user_id, "")
        self.assertEqual(b1.name, "")
        self.assertEqual(b1.description, "")
        self.assertEqual(b1.number_rooms, 0)
        self.assertEqual(b1.number_bathrooms, 0)
        self.assertEqual(b1.max_guest, 0)
        self.assertEqual(b1.price_by_night, 0)
        self.assertEqual(b1.latitude, 0.0)
        self.assertEqual(b1.longitude, 0.0)
        self.assertEqual(b1.amenity_ids, [])

        self.assertTrue(isinstance(b1.city_id, str))
        self.assertTrue(isinstance(b1.user_id, str))
        self.assertTrue(isinstance(b1.name, str))
        self.assertTrue(isinstance(b1.description, str))
        self.assertTrue(isinstance(b1.number_rooms, int))
        self.assertTrue(isinstance(b1.number_bathrooms, int))
        self.assertTrue(isinstance(b1.max_guest, int))
        self.assertTrue(isinstance(b1.price_by_night, int))
        self.assertTrue(isinstance(b1.latitude, float))
        self.assertTrue(isinstance(b1.longitude, float))
        self.assertTrue(isinstance(b1.amenity_ids, list))

        self.assertTrue(hasattr(b1, "city_id"))
        self.assertTrue(hasattr(b1, "user_id"))
        self.assertTrue(hasattr(b1, "name"))
        self.assertTrue(hasattr(b1, "description"))
        self.assertTrue(hasattr(b1, "number_rooms"))
        self.assertTrue(hasattr(b1, "number_bathrooms"))
        self.assertTrue(hasattr(b1, "max_guest"))
        self.assertTrue(hasattr(b1, "price_by_night"))
        self.assertTrue(hasattr(b1, "latitude"))
        self.assertTrue(hasattr(b1, "longitude"))
        self.assertTrue(hasattr(b1, "amenity_ids"))
