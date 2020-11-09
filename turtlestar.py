from turtle import *
t=Turtle()
#t.speed(1)

l=['red','blue','yellow','green','gold']
for i in range(500):
    t.pencolor(l[i%5])
    t.pensize(i%5)
    t.forward(100)
    t.left(216+i)
done()