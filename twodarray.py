from numpy import *
arr=array([
    [1,2,3],
    [4,5,6.0]
])

print(arr)

print(arr.dtype) # datatype of an array
print(arr.ndim) # dimension of ana array
print(arr.shape) # no of row and column
print(arr.size) # no of elemnts

# converting 2 d array into 1-d array

arr2=arr.flatten()
print(arr2)

arr3=array([
    [1,2,3,4,5,6],
    [3,3,3,3,3,3]
])
print(arr3.shape)

# converting 2d array into another shape
arr4=arr3.reshape(4,3)
print(arr4)
print(arr4.shape)

arr5=arr3.reshape(2,2,3)
print(arr5)
print(arr5.shape)