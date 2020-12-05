from tkinter import *
root=Tk()
root.title("Canvas")
canvas=Canvas(root,height=400, width=500, bg="red")
canvas.create_line(0,0,300,400,fill="yellow",width=10)
canvas.create_text(200,300,text="My canvas Example",fill="blue",font=("comic Sans Ms",13,"bold"))
canvas.create_rectangle(0,0,200,200,fill="white",outline="yellow", width=5)
canvas.create_oval(0,0,200,200,fill="blue",outline="yellow", width=5)
canvas.create_arc(0,0,200,200,fill="red",outline="yellow", width=5,extent=90)
point=[250,110,480,200,280,280,250,110]
poly=canvas.create_polygon(point,fill="gold",outline="black",width=5)
img=PhotoImage(file="test.gif")
canvas.create_image(300,300,image=img,anchor=SE)

canvas.pack()
root.geometry("600x600+120+20")
mainloop()