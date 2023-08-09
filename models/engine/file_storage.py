#!/usr/bin/python3
"""Module that defines FileStorage class"""
import json
from models.base_model import BaseModel

class FileStorage:
    """FileStorage class

    Attributes:
        file_path(str): path to the JSON file (ex: file.json)
        objects (dict): empty but will store all objects 
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns a dictionary of the objects."""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
            
            Args:
                obj: the object.
        """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dicts ={}
        for k,v in self.__objects.items():
            dicts[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dicts, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file does not exist,
        no exception should be raised)
        """
        #classes = {'BaseModel': BaseModel}    
        try:
            with open(self.__file_path, "r") as f:
                d = json.load(f)
                for k,v in d.items():
                    self.__objects[k] = globals()[v["__class__"]](**v)
        except FileNotFoundError:
            #print(self.__file_path + " file not found")
            pass

