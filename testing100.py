#!/usr/bin/python3
from models.base_model import BaseModel
import re
def gvs(ss):
    """quote the string when there is a whitespace in it

        Args:
        ss(str): string"""
    if not isinstance(ss, str):
        return ss
    for c in ss:
        if c.isspace() and (ss[0] != '"' or ss[-1] != '"'):
            return f'"{ss}"'
    return ss
def ReshapeCommand(s):
    """ convert <class name>.<command>() to <command> <class name>

    Args:
    s(str): string to reshape
    """
    if not re.match(r'\s*\w+\.\w+\(.*\)\s*$', s):
        # print("not a valid command")
        return [s]
    valid_comd_list = []
    fs = s.split(".")
    first = fs[0].lstrip()
    function_args = s[s.find("(") + 1:s.rfind(")")].strip()
    second = fs[1].split("(")[0]
    args = ""
    if function_args != "":
        try:
            args_dic = eval(function_args)
            if isinstance(args_dic, tuple):
                for e in args_dic:
                    s_e = e
                    if isinstance(e, dict):
                        for k, v in e.items():
                            comand = f'{second} {first} '
                            comand += f'{args_dic[0]} {gvs(k)} {gvs(v)}'
                            valid_comd_list.append(comand)
                        return valid_comd_list
                    args += f' {gvs(str(s_e))}'
            else:
                args += str(args_dic)
        except Exception as e:
            print("can't parse function args:" + str(e))
            return [s]
    valid_comd_list.append(f"{second} {first} {args}")
    return valid_comd_list


ss= """User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {})"""
print(ReshapeCommand(ss))