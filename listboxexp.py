from tkinter import *
root=Tk()

def get_data():
    x=l.curselection()
    print(x)
    for item in x:
        print(l.get(item))


def delete_data():
    x=l.curselection()
    print(x)
    for item in x:
        print(l.delete(item))
root.title("Listbox")
# Browse single multiple extented
l=Listbox(root,width=100,height=5,selectmode=EXTENDED)
l.insert(1,"Ramshyammohanrohanramehsuresh")
l.insert(2,"shyam")
l.insert(3,"C++")
l.pack()
btn=Button(root,text="get List data",command=get_data).pack()
btn2=Button(root,text="delete List data",command=delete_data).pack()
root.geometry("400x400+120+120")
mainloop()