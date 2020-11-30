from tkinter import *
root=Tk()
root.title("My First window")

label=Label(root,text="Enter Your Name",fg="red",bg="yellow",font=("Comic Sans Ms",15,"bold"))
label.pack()
root.geometry("400x500+400+100")
root.resizable(0,0)
root.mainloop()

