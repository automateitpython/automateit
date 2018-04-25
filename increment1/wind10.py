import pyautogui
import time
import ctypes, sys
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
import automateitcommon


def load():

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False    
    def about():
         root = tk.Tk()
         root.resizable(False, False)
         root.geometry("400x60")
         root.wm_title("Automate It - Windows Version")
         Label = tk.Label(root, text = 'Created by Brendan Rodgers', font = ('Comic Sans MS',10))
         Label.pack()
         Label2 = tk.Label(root, text = 'This application has been created for my final year project', font = ('Comic Sans MS',10))
         Label2.pack()

    file = open("distro.txt")
    data = file.read()
    file.close()

    screensizeout = str(pyautogui.size())

    def gui_input(prompt):

        root = tk.Toplevel()
    # this will contain the entered string, and will
    # still exist after the window is destroyed
        var = tk.StringVar()

    # create the GUI
        label = tk.Label(root, text=prompt)
        entry = tk.Entry(root, textvariable=var)
        label.pack(side="left", padx=(20, 0), pady=20)
        entry.pack(side="right", fill="x", padx=(0, 20), pady=20, expand=True)

    # Let the user press the return key to destroy the gui 
        entry.bind("<Return>", lambda event: root.destroy())

    # this will block until the window is destroyed
        root.wait_window()

    # after the window has been destroyed, we can't access
    # the entry widget, but we _can_ access the associated
    # variable
        value = var.get()
        return value
    
    def print_to_gui(text_string):
        status_label.config(text=text_string)
        root.update()

    def shutdowntime():
        os.system("shutdown /s /t " + gui_input("Please insert time in seconds for shutdown") )
    def restarttime():
        os.system("shutdown /r /t " + gui_input("Please insert time in seconds for shutdown") )
    def logouttime():
        os.system("shutdown /l /t " + gui_input("Please insert time in seconds for shutdown") )
    def cancel():
        os.system("shutdown /a")
        print_to_gui("Shutdown stopped sucessfully")

    
    def networkreset():
        if is_admin():
            print("")
        else:
    # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
            os.system("ipconfig /release")
            print_to_gui("Network Disconnected")
            os.system("ipconfig /renew")
            print_to_gui("Network Reconnected")

    def weather():
        os.system("cd C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        os.system("START /MAX chrome.exe")

    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("1200x600")
    root.wm_title("Automate It - Windows Version")
    Label = tk.Label(root, text = 'Automate It - Windows Version', font = ('Comic Sans MS',18))
    Label2 = tk.Label(root, text = 'Shutdown Functions', font = ('Comic Sans MS',8))
    Label3 = tk.Label(root, text = 'Voice Command', font = ('Comic Sans MS',8))
    Label4 = tk.Label(root, text = 'Network Commands', font = ('Comic Sans MS',8))
    Label5 = tk.Label(root, text = 'General Functions', font = ('Comic Sans MS',8))
    Results = tk.Label(root, text = "Your operating system is:" + data, font = ('Comic Sans MS', 12))
    screensize = tk.Label(root, text = "Screen Resolution is:" + screensizeout, font = ('Comic Sans MS', 12))
    button = tk.Button(root, text="Timed PC Shutdown", command=shutdowntime)
    button2 = tk.Button(root, text="Voice Command", command=about)
    button3 = tk.Button(root, text="Voice Command 2", command=about)
    button4 = tk.Button(root, text="Timed PC Restart", command=restarttime)
    button5 = tk.Button(root, text="Timed PC Logout", command=logouttime)
    button6 = tk.Button(root, text="Cancel Command", command=cancel)
    button7 = tk.Button(root, text="Reset Network Adapter", command=networkreset)
    button8 = tk.Button(root, text="Reset Network Adapter", command=weather)
    S = Scrollbar(root)
    T = Text(root, height=4, width=50)
    T.grid(row=5, column=1)
    T.config(yscrollcommand=S.set)
    filename = "Log.txt"
    with open(filename, 'r') as f:
        T.insert(INSERT, f.read())
    menubar = Menu(root)
    menubar.add_command(label="About", command=about)
    Label2.grid(row=0, column=1)
    button.grid(row=1, column=1)
    Label3.grid(row=0, column=4)
    Label4.grid(row=0, column=2)
    Label5.grid(row=0, column=3)
    button2.grid(row=1, column=4)
    button3.grid(row=2, column=4)
    button4.grid(row=2, column=1)
    button5.grid(row=3, column=1)
    button6.grid(row=4, column=1)
    button7.grid(row=1, column=2)
    button8.grid(row=1, column=3)
    status_label = tk.Label(text="")
    status_label.grid(row = 5, column = 1, pady = 50)
    Results.grid(row = 6, column = 1, pady = 330)
    screensize.grid(row = 6, column = 5, pady = 330, padx = 370)
    root.config(menu=menubar)
    root.mainloop()
