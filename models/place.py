#!/usr/bin/python3
"""Module that defines Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class.

    Attributes:
        city_id(str) : string
        user_id(str) : string
        name(str) : string
        description(str) : string
        number_rooms(int) : int
        number_bathrooms(str) : string
        max_guest(int) : int
        price_by_night(int) : int
        latitude(int) : int
        longitude(int) : int
        amenity_id(list) : list
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Instantiation
        """
        super().__init__(*args, **kwargs)
