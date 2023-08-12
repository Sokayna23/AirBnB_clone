#!/usr/bin/python3
""" BaseModel module """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ class BaseModel

    Attributes:
    id(str): unique id
    created_at(datetime): time of creation
    updated_at(datetime): time of updating

    Methods:
    __str__ : return class name
    save: save
    to_dict: return dict representation

    """

    def __init__(self, *args, **kwargs):
        """ init function

        Args:
        args: args
        kwargs: keywords args

        """
        if len(kwargs) == 0:
            # create a new object
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            # restore from dict
            # print("restoring object from dict")
            for key, value in kwargs.items():
                if key != "__class__":
                    self.__dict__[key] = value

            self.created_at = datetime.strptime(kwargs["created_at"],
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """ str function"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ save changes"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
