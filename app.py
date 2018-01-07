import os
from Tkinter import *

from targets_repo import TargetsRepo


def get_handler():
    if os.name == 'nt':
        from windows_handler import WindowsHandler
        return WindowsHandler
    elif os.name == 'posix':
        from mac_handler import MacHandler
        return MacHandler
    else:
        print "OS not supported yet: " + os.name
        exit(-1)


root = Tk()
root.resizable(0, 0)
root.title("Start...")
root.geometry("500x200")

target_repo = TargetsRepo()

def get_select_options(input):
    return target_repo.get_targets(input)
    # return [input + "-A", input + "-B", input + "-C"]


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
        # listbox.select_set(0)
        return "break"
    elif event.keysym == 'Return':
        go_to_selected_target()


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
        go_to_selected_target()


def clean_input():
    sv.set('')
    on_text_change(sv)


def on_type_anywhere(event):
    print event.keysym
    if event.keysym == 'Escape':
        clean_input()


def go_to_selected_target():
    item = listbox.get(ACTIVE)
    if item:
        get_handler().go_to('http://google.com/search?q=' + item)


sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: on_text_change(sv))
entry = Entry(root, textvariable=sv)
entry.bind('<Key>', on_type_in_entry)
entry.pack(fill=X)

listbox = Listbox(root)
listbox.pack(fill=X)
listbox.insert(END, "type a keyword")
listbox.bind('<Key>', on_type_on_list_box)

root.bind('<Key>', on_type_anywhere)

entry.focus_set()

get_handler().register_hot_key()

root.mainloop()
