from tkinter import *
from tkinter import  simpledialog
root=Tk()

def get_data():
    result=text.get(1.0,END)
    print(result)

def get_data1():
    result=text.selection_get()
    print(result)

def get_data2():
    result=text.selection_get()
    print(result)
    pos=text.search(result,1.0,stopindex=END)
    print(pos)

def get_data3():
    text.delete(1.0,END)

text=Text(root,width=25, height=10,wrap=WORD,padx=10,pady=10, selectbackground="red")
text.insert(INSERT,"Welcome you All.")
text.pack()
btn=Button(root,text="text value",command=get_data).pack()
btn2=Button(root,text="Selected text value",command=get_data1).pack()
btn3=Button(root,text="Selected text value index",command=get_data2).pack()
btn4=Button(root,text="clear text box",command=get_data3).pack()
root.geometry("400x400+120+120")
mainloop()