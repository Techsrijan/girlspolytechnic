from functools import reduce
def add(a,b):
    return a+b

print(add(4,6))

# how can we declare a function without name?
# this can be declared using lambda expression
# it can take any number of argument but have only one line code

# the above function can be declared as lambda
f=lambda a,b:a+b
print(f(50,100))


def is_even(n):
    return n%2==0
# filter map and reduce
num=[1,5,7,4,8,9,33,44,22,66,67]
#even=list(filter(is_even,num))

even=list(filter(lambda n:n%2==0,num))

print(even)

aftermap=list(map(lambda n:n+10,even))

print(aftermap)

# reduce converting more than one value in to one
even_sum=reduce(lambda a,b:a+b,aftermap)
print(even_sum)