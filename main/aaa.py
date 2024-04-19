from time import sleep

import win32api
import win32gui
import win32con

sleep(1)
tempWindowName = win32gui.GetWindowText(win32gui.GetForegroundWindow())
print(tempWindowName)
sleep(2)
hwndMain = win32gui.FindWindow("Notepad", tempWindowName)
hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
hwndEdit = win32gui.FindWindowEx(hwndMain, hwndChild, "Edit", "test - Notepad")


# while True:
#     temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x44, 0)
#     print(temp)
#     sleep(1)
