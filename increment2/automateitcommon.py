import pyautogui
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
from time import ctime
import os
from gtts import gTTS
import subprocess
import distro

import pyaudio
import gui
import time



def clear():
    selectall()
    removetext()

def submit():
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

def wait():
    time.sleep(2)

def threetab():
     pyautogui.press('tab')
     pyautogui.press('tab')
     pyautogui.press('tab')


def maximise(key1, key2):
    pyautogui.hotkey(key1, key2)

def waittomax():
    time.sleep(3)

def selectall():
    pyautogui.hotkey('ctrl', 'a')

def removetext():
    pyautogui.keyDown('backspace')
    pyautogui.keyUp('backspace')

def email(url):
    os.system("START /MAX chrome.exe")
    waittomax()
    x, y = pyautogui.locateCenterOnScreen('chromeaddressbar1366x768.png')
    print (x, y)
    pyautogui.click(x, y)
    clear()
    pyautogui.typewrite(url)
    submit()
