#!/usr/bin/python3
"""testing BaseModel"""
from models.place import Place
import unittest


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
        self.assertNotEqual(b1.city_id, "")
        self.assertNotEqual(b1.user_id, "")
        self.assertNotEqual(b1.name, "")
        self.assertNotEqual(b1.description, "")
        self.assertNotEqual(b1.number_rooms, 0)
        self.assertNotEqual(b1.number_bathrooms, 0)
        self.assertNotEqual(b1.max_guest, 0)
        self.assertNotEqual(b1.price_by_night, 0)
        self.assertNotEqual(b1.latitude, 0.0)
        self.assertNotEqual(b1.longitude, 0.0)
        self.assertNotEqual(b1.amenity_ids, [])
