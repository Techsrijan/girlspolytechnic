import math
print(math.sqrt(36))

def person(name,age,qual="High school"):
    print("name=",name)
    age=age+10
    print("age=",age)
    print("qualification=",qual)
#1. postional arguments
person("Ram",55)
#person(41,"abc")
person("abc",41)

'''
We can pass value inside function by four methods
1. postional arguments
2. keyword argument
3  variable length argument 
4  keyword variable length argument 

'''

#2. keyword argument
person(name="preeti",age=88)
person(age=55,name="rohan",qual="Inter")

#3  variable length argument

def add(x,*y):
    print(x)
    print(y)
    c=x
    for i in y:
        c=c+i
    return c
w=add(88,1,2,3)
print(w)

'''t=(5,4,6,8)
for i in t:
    print(i)'''

def add1(*y):
    print(y)
    c=0
    for i in y:
        c=c+i
    return c
w=add1(88,1,2,3)
print(w)


def fbdata(name,**data):
    print(name)
    #print(data)
    for i,j in data.items():
        print(i,j)

fbdata('Ram',age=25,city='gkp',mob='99656')

