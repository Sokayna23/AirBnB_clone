#!/usr/bin/python3
"""
Module that defines User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.

    Attributes:
        email (str): email of the user
        password (str): password of the user
        first_name (str): first_name of the user
        last_name (str): last_name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        init constructor

        Args:
        args(dict): args
        kwargs(dict): keyword args
        """
        super().__init__(*args, **kwargs)
