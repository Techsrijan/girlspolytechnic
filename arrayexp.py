from array import *
import time
marks = array('f',[1,2,3,4])
#marks = array('f',[1,2,3,4,5.6])
print(marks)

print(marks.buffer_info())

#marks.reverse()
print(marks)

for i in marks:
    print(i)

print(len(marks))

for i in range(len(marks)):
    time.sleep(1)
    print("index=",i,"value=",marks[i])

print(type(marks))
print(marks.typecode)

i=0
while i<len(marks):
    print(marks[i])
    i=i+1