from turtle import *

def draw():
    for i in range(4):
        t.forward(100)
        t.left(90)
t=Turtle()
s=Screen()
s.title("My first Turtle Program")
#s.bgcolor('blue')
#s.bgpic('test.gif')
t.speed(1)
t.shape('turtle')
#t.pencolor('red')
#t.fillcolor('green')
t.hideturtle()
t.pensize(10)
t.color('red','green')
t.fillcolor('gold')
t.begin_fill()
'''t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
'''
draw()
t.end_fill()

t.right(90)
t.penup()
t.forward(100)
t.pendown()
t.begin_fill()
draw()
t.end_fill()

done()