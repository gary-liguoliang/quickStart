from Tkinter import *
from _ctypes import byref
from ctypes import WinDLL, wintypes
import win32con

user32 = WinDLL('user32', use_last_error=True)


def register_hot_key():
    if not user32.RegisterHotKey(None, 1, win32con.MOD_ALT, win32con.VK_SPACE):
        print "failed to register hot key"
    else:
        print 'key registered'


def raise_above_all(window):
    window.lift()
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)
    window.after(1, lambda: window.focus_force())


def hotkey_handler(window):
    msg = wintypes.MSG()
    if user32.GetMessageA(byref(msg), None, 0, 0) != 0:
        if msg.message == win32con.WM_HOTKEY:
            if msg.wParam == 1:
                print("hotkey pressed")
                raise_above_all(window)

    user32.TranslateMessage(byref(msg))
    user32.DispatchMessageA(byref(msg))
    window.after(1, hotkey_handler, window)
