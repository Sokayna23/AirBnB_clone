#!/usr/bin/python3
"""Module that defines State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class.
    Attributes:
        name (str): name of the state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        init constructor
        """
        super().__init__(*args, **kwargs)
