import time

import cv2
import mss
import numpy as np
import pytesseract as pytesseract
import win32api
import win32gui
import win32process
import pyautogui
import win32com.client as comclt
from numpy import asarray
from playsound import playsound
import keyboard
import os
from PIL import ImageGrab


def get_current_layout(cls):
    # Get the current window's keyboard layout.
    thread_id = win32process.GetWindowThreadProcessId(
        win32gui.GetForegroundWindow()
    )[0]
    return win32api.GetKeyboardLayout(thread_id)


def screen_shot(left=0, top=0, width=1920, height=1080):
    stc = mss.mss()
    scr = stc.grab({
        'left': left,
        'top': top,
        'width': width,
        'height': height
    })

    img = np.array(scr)
    img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

    return img


def save_image():
    screenshot = screen_shot(730, 960, 230, 80)
    cv2.imshow('image', screenshot)
    cv2.waitKey(0)
    cv2.imwrite('new.jpg', screenshot)
    cv2.destroyAllWindows()


def fishing(key=''):
    wsh.AppActivate(tempWindowName)
    playsound('../Sounds/retro-game.wav')
    print(key)
    keyboard.press(key[0])
    keyboard.press(key[1])
    keyboard.press(key[2])
    time.sleep(0.1)
    keyboard.release(key[0])
    keyboard.release(key[1])
    keyboard.release(key[2])


def all_gray(folder=''):
    dir_list = os.listdir(folder)
    for i in dir_list:
        path = folder + '//' + i
        normal = cv2.imread(path)
        gray = cv2.cvtColor(normal, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(path, gray)


def read_text(img_path=''):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    test = cv2.imread(img_path)
    words_in_image = pytesseract.image_to_string(test)
    print(words_in_image)


def vision():
    screenshot = np.array(ImageGrab.grab(bbox=coord))


# keyboard.press('shift')
# keyboard.press('w')

time.sleep(0.2)
coord = (730, 960, 230, 80)
tempWindowName = win32gui.GetWindowText(win32gui.GetForegroundWindow())
playsound('../Sounds/retro-game.wav')
print(tempWindowName)

wsh = comclt.Dispatch("WScript.Shell")
aaa = True

while aaa:
    if pyautogui.locateOnScreen('Pics/DFG.jpg', grayscale=True) is not None:
        fishing('dfg')
    elif pyautogui.locateOnScreen('Pics/QWF.jpg', grayscale=True) is not None:
        fishing('qwf')
    elif pyautogui.locateOnScreen('Pics/QWR.jpg', grayscale=True) is not None:
        fishing('qwr')
    elif pyautogui.locateOnScreen('Pics/SDF.jpg', grayscale=True) is not None:
        fishing('sdf')
    elif pyautogui.locateOnScreen('Pics/ASF.jpg', grayscale=True) is not None:
        fishing('asf')
    time.sleep(0.3)

# while (True):
#     printscreen_pil = ImageGrab.grab()
#     printscreen_numpy = np.array(printscreen_pil.getdata(), dtype='uint8') \
#         .reshape((printscreen_pil.size[1], printscreen_pil.size[0], 3))
#     cv2.imshow('window', printscreen_numpy)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break

# words = pytesseract.image_to_string()
