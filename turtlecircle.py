from turtle import *
import time
t=Turtle()
s=Screen()
s.title("Circle Example")
s.setup(800,600)
'''t.circle(50)  # anticlockwise
t.circle((-100))
t.up()
t.forward(200)
t.down()
t.pencolor("red")
t.circle(300)
'''
t.circle(50)
t.up()
t.goto(-100,-100)
t.down()
t.circle(50)
t.undo()
t.reset()
time.sleep(2)
t.write("This is my turtle tutorial",font=("Comic Sans Ms",25,"bold"))
done()