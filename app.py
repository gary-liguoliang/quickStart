import os
import subprocess
from Tkinter import *

root = Tk()
root.resizable(0, 0)
root.title("Start...")
root.geometry("500x200")


def get_select_options(input):
    return [input + "-A", input + "-B", input + "-C"]


def update_select_options(input):
    listbox.delete(0, END)
    for item in get_select_options(input):
        listbox.insert(END, item)
    listbox.select_set(0)


def on_text_change(sv):
    print sv.get()
    update_select_options(sv.get())


def on_type_in_entry(event):
    if event.keysym in {'Up', 'Down'}:
        print "ignoring", event.keycode, event.keysym
        listbox.focus_set()
        listbox.select_set(0)
        return "break"


def on_type_on_list_box(event):
    print event.keycode, event.keysym
    if (len(event.keysym) == 1 and event.keysym.isalpha()):
        entry.focus_set()
        print "[input]key down: ", event.keysym
        sv.set(sv.get() + event.keysym)
        entry.icursor(len(sv.get()))
    elif (event.keysym == "BackSpace"):
        entry.focus_set()
        sv.set(sv.get()[:-1])
    elif (event.keysym == "Return"):
        if listbox.get(ACTIVE):
            go_to(listbox.get(ACTIVE))


def go_to(item):
    print "go to: ", item
    subprocess.call(['start',  'http://google.com/search?q=' + item], shell=True)


def register_key():
    if os.name == 'nt':
        import windows_ops
        windows_ops.register_hot_key()
        root.after(1, windows_ops.hotkey_handler, root)
    else:
        print "not supported yet"


sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: on_text_change(sv))
entry = Entry(root, textvariable=sv)
entry.bind('<Key>', on_type_in_entry)
entry.pack(fill=X)

listbox = Listbox(root)
listbox.pack(fill=X)
listbox.insert(END, "type a keyword")
listbox.bind('<Key>', on_type_on_list_box)

entry.focus_set()
register_key()
root.mainloop()
