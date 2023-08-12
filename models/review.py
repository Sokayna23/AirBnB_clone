#!/usr/bin/python3
"""Module that defines Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Review class.
        Attributes:
            place_id (str): place id.
            user_id (str): the user id.
            text (str): text.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        init constructor
        """
        super().__init__(*args, **kwargs)
