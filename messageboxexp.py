from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Message Box")
def call_me():
    #result=messagebox.askyesno("Confirmation message","Do you want to exit")
    result = messagebox.showwarning("Confirmation message","Do you want to exit")
    print(result)
    if result==True:
        print("Good bye")

btn=Button(root,text="Message", command=call_me).pack()
root.geometry("400x400+120+120")
mainloop()