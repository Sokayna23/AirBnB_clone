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

def gvs(ss):
    """gvs = get valid string;quote the string when there is a whitespace in it"""
    if not isinstance(ss,str):
        return ss
    for c in ss:
        if c.isspace() and (ss[0]!='"' or ss[-1]!='"'):
            return f'"{ss}"'
    return ss

def ReshapeCommand(s):
    """ convert <class name>.<command>() to <command> <class name>"""
    if re.match(r'\s*\w+\.\w+\(.*\)\s*$',s) == None:
        #print("not a valid command")
        return [s]
    valid_comd_list =[]
    fs = s.split(".")
    first = fs[0].lstrip()
    function_args = s[s.find("(")+1:s.rfind(")")].strip()
    second = fs[1].split("(")[0]
    args=""
    if function_args != "":
        try:
            args_dic = eval(function_args)
            if isinstance(args_dic,tuple):
                for e in args_dic:
                    s_e = e
                    if isinstance(e,dict) :
                        for k,v in e.items():
                            comand= f'{second} {first} {args_dic[0]} {gvs(k)} {gvs(v)}'
                            valid_comd_list.append(comand)
                        return valid_comd_list
                    args+= f' {gvs(str(s_e))}'
            else:
                args += str(args_dic)
        except Exception as e:
            print("can't parse function args:"+str(e))
            return [s]
    valid_comd_list.append(f"{second} {first} {args}")
    return valid_comd_list

ss = """User.update2("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})"""
ss1="""User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")"""
ss11="""User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John smith")"""
ss2 = """User.all()"""
ss3= """User.count()"""
ss4= """User.show(45)"""
ss5  ="""User.update(3f88b79a-e851-4711-8b8a-b3c044efb1ee, moi, "abdel mo")"""
ss6 ="""add"""
cc = ReshapeCommand(ss6)
for i in cc:
    print(i)

