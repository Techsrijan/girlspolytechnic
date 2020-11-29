class A:
    def __init__(self):
        print("I am class a Constructor")

class B(A):
    def __init__(self):
        super().__init__() # call the constructor of base class
        print("I am class b Constructor")

b=B()
