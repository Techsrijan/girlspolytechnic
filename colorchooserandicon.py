from tkinter import *
from tkinter import colorchooser
root=Tk()
root.title("My First window")
def color_chooser():
    c=colorchooser.askcolor()
    print(c[1])
    root.configure(background=c[1])

root.wm_iconbitmap("notepad.ico")
btn=Button(root,text="Color Chooser", command=color_chooser).pack()
root.geometry("400x500+400+100")
root.resizable(0,0)
root.mainloop()