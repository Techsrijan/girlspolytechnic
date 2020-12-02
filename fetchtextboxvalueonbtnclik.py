from tkinter import *
root=Tk()
root.title("My First window")
def get_textbox_data():
    p=x.get()
    #print(p,type(p))
    y = StringVar()
    label = Label(root,textvariable=y)
    label.place(x=150, y=50)
    y.set(p)



x=StringVar()
entry=Entry(root,textvariable=x)
entry.place(x=50,y=50)

btn1=Button(root,text="Button1",fg="red",bg="yellow",font=("Comic Sans Ms",15,"bold"),command=get_textbox_data)
btn1.place(x=100,y=100)

root.geometry("400x500+400+100")
root.resizable(0,0)
root.mainloop()