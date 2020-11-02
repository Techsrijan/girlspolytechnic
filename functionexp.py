# function declaration
def welcome():
    print("Good morning")
    print("thank you")


welcome()    #function call
welcome()
print("Third time call")
welcome()

'''def add():
    a,b=5,6
    c=a+b
    print("Sum=",c)'''


def add(a,b):
    c=a+b
    print("Sum=",c)

def calc(x,y):  # here x and y are called fromal argument
    s=x*y
    t=x-y
    return s,t

add(4,9)
welcome()

p,q=calc(2,4)    # p,q=s,t
print("Mul=",p)
print("Sub=",q)

m=int(input("enter first number"))
n=int(input("enter second number"))
p,q=calc(m,n)#here m and n are called actual argumnet
print("Mul=",p)
print("Sub=",q)
