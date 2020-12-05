from tkinter import *
root=Tk()
root.title("My First window")

def msg(event=""):
    print("Good morning")


root.bind("<Control-M>",msg)
entry=Entry(root)
entry.place(x=50,y=50)
btn1=Button(root,text="Button1",fg="red",bg="yellow",font=("Comic Sans Ms",15,"bold"),command=msg)
btn1.place(x=100,y=100)
quitbutton = Button(root, text="Close Me", command=quit)
quitbutton.pack()
root.geometry("400x500+400+100")
root.resizable(0,0)
root.mainloop()