#!/usr/bin/python3

v = "-78.0"
def CastedToType(v):
    try:
        v = int(v)
        print("it's a int")
    except ValueError:
        try:
            v = float(v)
            print("it's a float")
        except ValueError:
            print("it's a string")
            pass
    return v
print(CastedToType("az"))