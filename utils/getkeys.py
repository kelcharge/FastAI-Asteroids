import win32api as wapi
import win32con
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\0x25":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
        elif wapi.GetAsyncKeyState(win32con.VK_LEFT):
            keys.append("Left")
        elif wapi.GetAsyncKeyState(win32con.VK_RIGHT):
            keys.append("Right")
    if 'H' in keys:
        return 'H'
    elif 'B' in keys:
        return 'B'
    elif 'Left' in keys:
        return 'Left'
    elif 'Right' in keys:
        return 'Right'
    elif ' ' in keys:
        return ' '
    else:
        return ''