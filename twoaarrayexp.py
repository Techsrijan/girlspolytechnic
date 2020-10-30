from numpy import *

arr=array([1,2,3,4,5.0])
print(arr)

print(arr.dtype)

arr2=array([1,2,3,4,5],float)
print(arr2)
'''
There are six ways to create an array using numpy

1.by using array()
2. linspace
3.logspace
4.arange
5.zeros
6.ones
'''
arr3=linspace(1,5,5)
print(arr3)

arr4=logspace(1,5,5)
print(arr4)

arr5=arange(0,15,2)
print(arr5)

arr6=zeros(50)
print(arr6)

arr7=ones(20,int)
print(arr7)

print()
