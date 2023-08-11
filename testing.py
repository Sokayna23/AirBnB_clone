#!/usr/bin/python3
from models.base_model import BaseModel
"""
print("--------------------------__---------")
b1 = BaseModel()
print(" b1 ID : " + b1.id)
d1 = b1.to_dict()
print(" d1_dict   ")
print(d1)
b2 = BaseModel(**d1)
print("b2 ID: " + b2.id)
"""
class sun:
    id =78
    def __init__(self):
        pass
        #print(type(self).__name__)
    def venus(self):
        #print("venus")
        pass
class earth(sun):
    id =10
s = sun()
e = earth()


"""
def ReshapeCommand(string):
    " convert <class name>.<command>() to <command> <class name>"

    available_commands={"all":78}
    split1 = string.split(".")
    All
    if len(split1) != 2 or not split1[0].lstrip().isalnum():
        print("not a command")
    else:
        split2= split1[1].split("(")
        if len(split2) != 2 or not split2[0].isalnum() or \
        len(split2[1]) == 0 or split2[1].strip()[-1] != ")":
            print("not a command") 
            return
        
        print("it's a command")
 
ts=["User.all()","User. all()","User .all()", "   l.p( 88,74 )  "]
for t in ts:
    print("testing: #"+t+"#")
    ReshapeCommand(t)
    print("")
    """

import re
def ReshapeCommand(s):
    """ convert <class name>.<command>() to <command> <class name>"""
    print(re.match(r'\s*\w+\.\w+\(.*\)\s*$',ss).group())
    if re.match(r'\s*\w+\.\w+\(.*\)\s*$',ss) == None:
        print("not a command")
        return
    fs = s.split(".")
    first = fs[0].lstrip()
    function_args = s[s.find("(")+1:s.rfind(")")].strip()
    second = fs[1].split("(")[0]
    print("first#"+first+"#")
    print("second#"+second+"#")
    print("argument#"+function_args+"#")
ss = "User.cmd( {er:''})  "
#ReshapeCommand(ss)

ss ="User.all(4,n4, 'kjj')    "

ma = re.match("\s*\w+\.\w+\(.*\)\s*$",ss)
print(ma)
if   ma != None:
    print("it's a valide command")
else:
    print("not command")