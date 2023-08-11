#!/usr/bin/python3
from models.base_model import BaseModel

print("--------------------------__---------")
b1 = BaseModel()
print(" b1 ID : " + b1.id)
d1 = b1.to_dict()
print(" d1_dict   ")
print(d1)
b2 = BaseModel(**d1)
print("b2 ID: " + b2.id)
