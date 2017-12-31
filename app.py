from Tkinter import *

root = Tk()
w = Label(root, text="hello world")
w.pack()

e = Entry(root)
e.pack()

b = Button(root, text="run")
b.pack()


root.mainloop()
