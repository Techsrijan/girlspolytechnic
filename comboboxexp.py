from tkinter import *
from tkinter import ttk


def get_combo():
    r=c.get()
    print(r)
root=Tk()
root.title("Combobox")
#l=["UP","Bihar","Mp"]
l=list(range(1,32))
c=ttk.Combobox(root,value=l)
c.set("Select Your state")
c.pack()
btn=Button(root,text="get Combo data",command=get_combo).pack()
root.geometry("400x400+120+120")
mainloop()

