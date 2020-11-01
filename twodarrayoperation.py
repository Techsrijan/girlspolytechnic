from numpy import *
arr1=array([
    [1,2,3],
    [4,5,6.0]
])

arr2=array([
    [1,2],
    [4,5],
    [6,9]
])

#print(arr1+arr2)

#print(arr1*arr2)

a=matrix(arr1)
b=matrix(arr2)
print(a*b)


arr4=array([
    [1,2,14],
    [4,5,158],
    [6,9,15]
])
print(diagonal(arr4))
print(arr4.min())
print(arr4.max())

x=matrix('123;456;789')
print(x)
