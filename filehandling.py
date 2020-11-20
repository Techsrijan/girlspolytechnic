f=open("test.gif","rb")
print(f)
#to read the contents of file
#print(f.read())

for data in f:
    print(data,end="")

f1=open("shyam.txt","w")
print(f1)
msg=input("enter the text u want to write")
f1.write(msg)
f1.close()
