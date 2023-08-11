#!/usr/bin/python3

class a:
    def __init__(self):
        print("usign type")
        print(type(self).__name__)
        print("using class")
        print(self.__class__.__name__)   

class b(a):
    def __init__(self):
        super().__init__()

o1 = b()