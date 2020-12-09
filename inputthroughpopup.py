from tkinter import *
from tkinter import  simpledialog
root=Tk()

def get_popup():
    for i in range(4):
        s=simpledialog.askstring("Input Box","Enter your name")
        print(s)
btn=Button(root,text="spin value",command=get_popup).pack()
root.geometry("400x400+120+120")
mainloop()