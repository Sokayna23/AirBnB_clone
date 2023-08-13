#!/usr/bin/python3
from models.base_model import BaseModel




b1 = BaseModel()
d1= b1.to_dict()
print(b1.id)

b2 = BaseModel(**d1)
print(b2.id)
