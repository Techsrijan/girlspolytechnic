from tkinter import *
root=Tk()
root.title("My First window")
label=Label(root,text="Enter your Name")
label.grid(row=0,column=0)
txt=Entry(root)
txt.grid(row=0,column=1)

labe2=Label(root,text="Enter your Password")
labe2.grid(row=1,column=0)
txt2=Entry(root,justify="right",bd=15,insertwidth="5",show="*")
txt2.grid(row=1,column=1)

btn=Button(root,text="Login")
btn.grid(row=2,columnspan=2)
root.resizable(0,0)
root.mainloop()