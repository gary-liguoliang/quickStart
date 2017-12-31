import os
from Tkinter import *
from ttk import Combobox

root = Tk()


def on_field_change(index, value, op):
    print "combobox updated to: ", cb.get()
    cb.bind("<Down>", lambda e: None)


v = StringVar()
v.trace('w', on_field_change)

cb = Combobox(root, textvar=v, values=("one", "two", "three"))
cb.pack()
cb.focus()

if os.name == 'nt':
    import windows_ops

    windows_ops.register_hot_key()
    root.after(1, windows_ops.hotkey_handler, root)

root.mainloop()
