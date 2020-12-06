from tkinter import *
root=Tk()
def get_data():
    print(i.get())
    print(j.get())
    if i.get()==1:
        print("Hindi")
    if j.get()==1:
        print("English")


f=LabelFrame(root,text="Select Your Known Language")
i=IntVar()
r1=Checkbutton(f,text="Hindi",variable=i)
j=IntVar()
r2=Checkbutton(f,text="English",variable=j)
r1.pack()
r2.pack()
btn=Button(f,text="get Check value",command=get_data).pack()
f.pack()
root.geometry("400x400+120+120")
mainloop()