import win32api, win32con, time, win32ui, pyHook, pythoncom

import datetime
import time
import sys

import threading, sys, os

repeat = True


import traceback
def OnKeyboardEvent(event):
    global repeat
    print "KEYBOARD EVENT"
    try:
        if event.Key == 'S' or event.Key == 's':
            repeat = False
            print "EXITING"
            os._exit(1)

        print event.Key
    except:
        print "EXITING"
        print traceback.print_exc()
        os._exit(1)

    return True



def pywinauto_click(x,y,mouse_button):
    import pywinauto.application

    app = pywinauto.application.Application()
    comapp = app.connect_(path = "explorer")

    for i in comapp.windows_():
        if "Progman" == i.FriendlyClassName():
            #i.MoveMouse(coords=(x + 1920, y))
            i.ClickInput(coords=(x + 1920, y), button=mouse_button)
            #i.ClickInput(coords=(x, y))


def click(x,y,mouse_button):

    win32api.SetCursorPos((x,y))
    if mouse_button == 'left':
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

    elif mouse_button == 'right':
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

def current_mouse_position():
    x, y = win32api.GetCursorPos()
    return x, y


def click_current_position():
    x, y = win32api.GetCursorPos()
    click(x,y,'left')
    print x,y



import random

from win32gui import GetWindowText, GetForegroundWindow, GetWindowRect
from win32api import GetSystemMetrics

def get_active_window():

    return GetForegroundWindow()

def get_window_name(window_handler):
    return GetWindowText(window_handler)

def generate_random_float(low_f, high_f):
    return random.uniform(low_f,high_f)


def contains_any(str1, treasure_list):
    for treasure in treasure_list:
        if treasure in str1:
            return True

    return False

def execute_actions_handler():
    global repeat

    time_inbetween_actions = 5

    count = 0
    while repeat:
        #time_inbetween_actions = generate_random_float(10, 25)

        p = Process(target=execute_actions, args=())
        p.start()
        p.join()

        count += 1


        #time.sleep(time_inbetween_actions)
        # if count > 31:
        #     #regular exit() doesnt close from inside threads
        #     os._exit(1)


import win32gui
def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst
#
# def find_window(title):
#     appwindows = get_app_list()
#     for i in appwindows:
#         if title in i[1]:
#             return i[0]
#     return None
#

# from pywinauto.findwindows    import find_window
# from pywinauto.win32functions import SetForegroundWindow
VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0}

def press_key(key_name):
    win32api.keybd_event(VK_CODE[key_name], 0,0,0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE[key_name],0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(random.uniform(0.0, 0.5))




def hold_click(x,y,mouse_button):
    win32api.SetCursorPos((x,y))
    if mouse_button == 'left':
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        time.sleep(10)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def hold_key(key_name):
    win32api.keybd_event(VK_CODE[key_name], 0,0,0)
    time.sleep(10)
    win32api.keybd_event(VK_CODE[key_name],0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(1)


import ctypes

z = 0
def execute_actions():
    global z
    global repeat

    time.sleep(3)
    while repeat:
        x, y = current_mouse_position()
        ctypes.windll.user32.keybd_event(VK_CODE['w'], 0, 0, 0)      #Key is down
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        time.sleep(5)
        ctypes.windll.user32.keybd_event(VK_CODE['w'], 0, 0x0002, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

execute_actions()

import multiprocessing
from multiprocessing import Process, Value, Array, freeze_support, Manager
import os

import sys
import pythoncom, pyHook
import threading
import os
import requests

if __name__ == '__main__':

    #BUILD STANDALONE EXECUTABLE:
    #pyinstaller -F automine.py

    multiprocessing.freeze_support()


    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()


    p = Process(target=execute_actions_handler, args=())
    p.start()

    try:
        pythoncom.PumpMessages()   #This call will block forever unless interrupted,
                               # so get everything ready before you execute this.

    except (KeyboardInterrupt, SystemExit) as e: #We will exit cleanly if we are told
        print(e)


        os._exit(1)





