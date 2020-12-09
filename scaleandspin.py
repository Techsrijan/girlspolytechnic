from tkinter import *
root=Tk()
def get_spin():
    print(s.get())
    print(sp.get())
root.title("Scale and spin")
s=Scale(root,sliderlength=50,from_=1,to=200,orient=HORIZONTAL,length=200,width=20)
s.set(100)
s.pack()

sp=Spinbox(root,from_=1, to=5)
sp.pack()
btn=Button(root,text="spin value",command=get_spin).pack()
root.geometry("400x400+120+120")
mainloop()