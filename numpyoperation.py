from numpy import *
arr=array([1,2,3,4,5])
print(arr)
arr=arr*2
print(arr)

arr2=array([55,1,66,1,99])
arr3=arr2+arr
print(arr3)

print(concatenate([arr,arr2]))
print(average(arr2))
print(sum(arr2))
print(max(arr2))
print(min(arr2))

# aliasing
arr4=arr2
print(arr4)

print(id(arr4))
print(id(arr2))

# what if want different address
arr5=array([55,66,889,555])
arr6=arr5.view()
print(arr5)
print(arr6)
print(id(arr5))
print(id(arr6))


arr5[1]=786
print(arr5[1])
print(arr5)
print(arr6)
# the above procedure is called shallow copy

# what if u want different address as well as does not effect
# each other on change
# for this we will use deep copy

arr7=array([88,99,66,44,66,2])
arr8=arr7.copy()
print(arr7)
print(arr8)
print(id(arr7))
print(id(arr8))

arr7[1]=786
print(arr7[1])
print(arr7)
print(arr8)
