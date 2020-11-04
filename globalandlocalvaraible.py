x=10 #global


def msg():
    a=5 #local
    print(a,x)

msg()
print(x)

# what if u want to declarea ariable inside
#  but behaves as global

def test():
    p=5
    global y
    y=10
    print(p,y)

test()
print(y)

r=100
s=600
def magic():
    r=100
    print(r)
    print(id(r))
    w=globals()['r']
    print(id(w))
    print(w)

magic()

