def mul(x,y):
    print(x*y)
def sub(x,y):
    print(x-y)


sub(2,5)
mul(4,6)
'''
special variable __name__
'''
print(__name__)

if __name__=="__main__":
    def add(x, y):
        print(x + y)
    add(5,2)
else:
    print("Callling not allowed")
