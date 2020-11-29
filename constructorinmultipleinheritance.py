class A:
    def __init__(self):
        print("I am class a Constructor")

class B:
    def __init__(self):
       print("I am class b Constructor")

class C(B,A):    #MRO method resolution order - left to right
    def msg(self):
        print("Class C")


c=C()
c.msg()