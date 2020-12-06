from tkinter import *
root=Tk()
def get_data():
    if i.get()==1:
        print("Male")
    else:
        print("Female")

f=LabelFrame(root,text="Select You Gender")
i=IntVar()
r1=Radiobutton(f,text="male",value=1,variable=i)
r2=Radiobutton(f,text="Female",value=2,variable=i)
r1.pack()
r2.pack()
btn=Button(f,text="get radio value",command=get_data).pack()
f.pack()
root.geometry("400x400+120+120")
mainloop()