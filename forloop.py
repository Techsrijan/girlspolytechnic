for i in range(10):
    print(i)
    if i%2==0:
        print("even")
    else:
        print("odd")

for j in range(5,20):
    print(j,end="")

print()
for k in range(5,20,2):
    print(k,end="")

print()
for k in range(-20,5,1):
    print(k,end="")


print()
i=-20
while i<5:
    print(i,end="")
    i=i+1

print(" prime No check")
n=7
for p in range(2,n):
    if n%p==0:
        print("not Prime")
        break
    else:
        print("Prime no")


print(" prime No check second time")
n=7
for p in range(2,n):
    if n%p==0:
        print("not Prime")
        break
else:
    print("  Prime no")

