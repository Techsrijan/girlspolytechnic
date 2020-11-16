import time
print("Time in second since 1970=",time.time())

# in the form of tuple
print(time.localtime(time.time()))

print(time.asctime())

t=(2020,11,16,7,28,27,0,321,0)

print(time.mktime(t))

