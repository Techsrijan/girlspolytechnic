s="welcome,to, Techsrijan, THANKS"
'''
print(s)
print(s[0:])
print(s[0::2])
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.title())
print(s.swapcase())
st=s.split(',')
for i in st:
    print(i)

str="Her name is Tamanna and Tamanna is good girl"
print(str)
x=input("Enter the word you want to find")
print(x)
y=str.find(x)
if y==-1:
    print("word not found")
else:
    print("Word found at location:",y)
    rep=input("enter the word you want to replace")
    str2=str.replace(x,rep)
    print(str2)
'''

name="humtum"
print(name.isdigit())
print(name.isalpha())

name2="123"
print(name2.isdigit())

email="aswani123"
print(email.isalnum())

name3=input("Enter your name")
print(name3)
print(name3.strip())

name4="      hello         "
print(name4,end="")

print("World")
print(name4.lstrip())
print(name4.rstrip(),end="")
print("test")
