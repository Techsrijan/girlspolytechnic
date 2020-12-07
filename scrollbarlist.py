from tkinter import *
root=Tk()
f=Frame(root)
scroll=Scrollbar(f)
scroll.pack(side=RIGHT,fill=Y)
l=Listbox(f,selectmode=EXTENDED,yscrollcommand=scroll.set)
for i in range(1,100):
    l.insert(END,"MY VALUE"+str(i))
l.pack()
scroll.config(command=l.yview)
f.pack()
root.geometry("400x400+120+120")
mainloop()