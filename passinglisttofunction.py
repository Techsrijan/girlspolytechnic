def counter(l):
    even=odd=0
    for i in l:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    return even,odd
l=[5,2,7,9,14,21,24,25]
x,y=counter(l)
print(x,y)
print("No of even=:{} and no of odd=:{}".format(x,y))