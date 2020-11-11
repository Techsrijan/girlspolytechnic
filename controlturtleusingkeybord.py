from turtle import *
t=Turtle()
s=Screen()
def moveForward():
    t.forward(100)
def moveBackward():
    t.backward(100)
def moveLeft():
    t.left(90)
def moveRight():
    t.right(90)

s.onkey(moveForward,"D")
s.onkey(moveBackward,"Down")
s.onkey(moveLeft,'Left')
s.onkey(moveRight,"Right")
s.listen()
done()