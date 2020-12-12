from tkinter import *
from tkinter import filedialog
root=Tk()
root.title("My First window")
def open_file():
    result=filedialog.askopenfile(initialdir="/",title="open file",
                                  filetypes=(("Text File","*.txt"),("All files","*.*")))
    print(result)
    for data in result:
        print(data)
        text.insert(INSERT, data)

def save_file():
    f=filedialog.asksaveasfile(mode="w",defaultextension="*.txt")
    if f is None:
        return
    f.write("Happy b-day")

root.wm_iconbitmap("notepad.ico")
text=Text(root,width=25, height=10,wrap=WORD,padx=10,pady=10, selectbackground="red")

text.pack()
btn=Button(root,text="open file", command=open_file).pack()
btn2=Button(root,text="save file", command=save_file).pack()
root.geometry("400x500+400+100")
root.resizable(0,0)
root.mainloop()