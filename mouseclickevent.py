from tkinter import *
root=Tk()
root.title("My First window")

def msg1(event):
    print("Good morning")

def msg2(event):
    print("Good Afternoon")

def msg3(event):
    print("Good evening")



btn1=Button(root,text="Button1",fg="red",bg="yellow",font=("Comic Sans Ms",15,"bold"))
btn1.place(x=100,y=100)
btn2=Button(root,text="Button2",fg="red",bg="yellow",font=("Comic Sans Ms",15,"bold"))
btn2.place(x=100,y=200)
btn3=Button(root,text="Button2",fg="red",bg="yellow",font=("Comic Sans Ms",15,"bold"))
btn3.place(x=100,y=300)
btn1.bind("<Button-1>",msg1)
btn2.bind("<Button-2>",msg2)
btn3.bind("<Button-3>",msg3)
root.geometry("400x500+400+100")
root.resizable(0,0)
root.mainloop()