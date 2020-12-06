from tkinter import *
root=Tk()
def open_window():
    top=Toplevel()
    top.title("Child window")
    btn2 = Button(top, text="close", command=top.destroy).pack()
    top.geometry("400x400+120+120")


root.title("Top level window")
btn=Button(root,text="open new window",command=open_window).pack()
btn2=Button(root,text="close",command=quit).pack()
root.geometry("400x400+120+120")
mainloop()