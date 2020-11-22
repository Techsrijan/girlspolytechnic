#set is unordered collection of unique data
'''
marks={11,12,55,55,9,6,7,9}
print(marks,type(marks))

marks.add(100)
print(marks)

marks.remove(6)
print(marks)

marks.remove(6)
print(marks)


fruit=frozenset([3,5,6,6,7,8])
print(fruit)

#fruit.add('100')

a={}
print(type(a))

b=set()
print(type(b))
print(b)

b=set(marks)
print(b)

x= 100 in marks
print(x)

y= 88 not in marks
print(y)

p={4,5,6,7,8}
q={1,2,3,4,5}

# union
print(p|q)

#intersection
print(p&q)

# difference
print(p-q)
print(q-p)

#symmetric difference
print(p^q)

print(len(p))

# to clear the set
print(p)
print(p.clear())
print(p)
'''

d={}
print(type(d))

dic={'ashwani':44,'mohan':55,'rohan':55,'rohit':99}
print(dic)

print(d)

college=dict()
print(college,type(college))

temp=dict(dic)
print(temp)

print(d)
d['aradhna']='Samsung'
d['khusboo']='Mi'
d['Rohaan']='Nokia'
print(d)

print(len(d))

print(d.keys())
print(d.values())

# membership operator
print('khusbooo' in d)
print('khusbooo' not in d)

print(d)
del d['Rohaan']

print(d)

print(d.clear())