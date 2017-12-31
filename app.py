import os
from Tkinter import *

import windows_ops

root = Tk()
w = Label(root, text="hello world")
w.pack()

e = Entry(root)
e.pack()

b = Button(root, text="run")
b.pack()

if os.name == 'nt':
    windows_ops.register_hot_key()
    root.after(1, windows_ops.hotkey_handler, root)

root.mainloop()
