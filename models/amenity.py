#!/usr/bin/python3
"""
Module that defines Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class."""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        init constructer
        """
        super().__init__(*args, **kwargs)
