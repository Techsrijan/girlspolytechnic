from turtle import *
t=Turtle()
t.up()
t.goto(200,0)
t.down()
t.pensize(10)
l=['red','green','gold','yellow','blue']
for i in range(5):
    t.pencolor(l[i])
    t.circle(40)
    t.up()
    t.backward(40)
    t.down()
    #t.circle(20)
done()