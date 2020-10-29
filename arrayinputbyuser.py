from array import *
num=int(input("enter the number of elements"))
a=array('i',[]) # create an empty array
for i in range(num):
    x=int(input("Enter the elements of an integer array"))
    a.append(x)

print(a)  # print the elements of an array

search=int(input("Enter the element you want to find"))

j=0
for k in a:
    #print(k)
    if k==search:
        print("Item found at position=",j)
        break

    j=j+1
else:
    print("Item not found ")


# using python
print("Item found at position=",a.index(search))