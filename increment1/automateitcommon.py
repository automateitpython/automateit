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


def clear():
    selectall()
    removetext()

def submit():
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

def enterurl(url):
    pyautogui.typewrite(url)


def maximise(key1, key2):
    pyautogui.hotkey(key1, key2)

def waittomax():
    time.sleep(3)

def selectall():
    pyautogui.hotkey('ctrl', 'a')

def removetext():
    pyautogui.keyDown('backspace')
    pyautogui.keyUp('backspace')
