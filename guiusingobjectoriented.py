from tkinter import *

class GUI:
    def msg(self):
        print("Good morning")

    def __init__(self,window):
        self.window=window
        self.button=Button(window,text="Click Me",command=self.msg)
        self.button.pack()
        self.quitbutton = Button(window, text="Close Me", command=window.quit)
        self.quitbutton.pack()



root=Tk()
a=GUI(root)

mainloop()