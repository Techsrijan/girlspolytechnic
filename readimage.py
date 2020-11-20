f=open("test.gif","rb")
print(f)

for data in f:
    print(data,end="")

f2=open("nest.gif","wb")
for data in f:
    print(data)
    f2.write(data)

'''
f3=open("best.gif","rb")
print(f3)'''