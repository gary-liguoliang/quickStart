from Tkinter import *
from _ctypes import byref
from ctypes import WinDLL, wintypes
import win32con

root = Tk()
w = Label(root, text="hello world")
w.pack()

e = Entry(root)
e.pack()

b = Button(root, text="run")
b.pack()

user32 = WinDLL('user32', use_last_error=True)
if not user32.RegisterHotKey(None, 1, win32con.MOD_CONTROL, ord("G")):
    print "failed to register hot key"


def raise_above_all(window):
    window.lift()
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)
    window.after(1, lambda: window.focus_force())


def hotkey_handler(root):
    msg = wintypes.MSG()
    if user32.GetMessageA(byref(msg), None, 0, 0) != 0:
        if msg.message == win32con.WM_HOTKEY:
            if msg.wParam == 1:
                print("hotkey pressed")
                raise_above_all(root)

    user32.TranslateMessage(byref(msg))
    user32.DispatchMessageA(byref(msg))
    root.after(1, hotkey_handler, root)


root.after(1, hotkey_handler, root)

root.mainloop()
