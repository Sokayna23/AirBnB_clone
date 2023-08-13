#!/usr/bin/python3
"""Module that defines City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class.
    Attributes:
        state_id (str): state id.
        name (str): name of the city.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        init constructer
        """
        super().__init__(*args, **kwargs)
