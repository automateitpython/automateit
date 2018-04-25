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
import automateitcommon

def manjaro():

    pyautogui.FAILSAFE = True


# Display a string in `out_label`
    def print_to_gui(text_string):
        status_label.config(text=text_string)
    # Force the GUI to update
        root.update()

    def test():
       with open('distro.txt') as f:
            found = False
            for line in f:
                if "Manjaro" in line: # Key line: check if `w` is in the line.
                    subprocess.call(['/usr/bin/firefox'])
                    automateitcommon.waittomax()
                    pyautogui.press('f11')
                    automateitcommon.waittomax()
                    pyautogui.moveTo(600, 0)
                    x, y = pyautogui.locateCenterOnScreen('addressbar.png')
                    print (x, y)
                    pyautogui.click(x, y)
                    automateitcommon.clear()
                    automateitcommon.enterurl('gmail.com')
                    automateitcommon.submit()
                    found = True
                if not found:
                    print_to_gui('Could not load browser')
    def netreset():
        os.system("systemctl restart NetworkManager.service")

    status = [""]

    def emptytrash():
        os.system("rm -rf ~/.local/share/Trash/*")
        with open("Log.txt", "a") as text_file:
            text_file.write("Bin Successfully Emptied" + (ctime()) + '\n')
        print_to_gui("Bin Emptied Successfully - check log file for more details",)


    def speak(audioString):
        print(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")

    def recordAudio():
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        data = ""
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = r.recognize_google(audio)
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return data

    def jarvis(data):
        if "load email" in data:
            test()

        if "what time is it" in data:
            speak(ctime())

        if "how are you" in data:
            speak("I am fine")

    def ask():
        time.sleep(2)
        speak("Hi, what can I do for you?")
        while 1:
            data = recordAudio()
            jarvis(data)

    def about():
         root = tk.Tk()
         root.resizable(False, False)
         root.geometry("400x60")
         root.wm_title("Automate It")
         Label = tk.Label(root, text = 'Created by Brendan Rodgers', font = ('Comic Sans MS',10))
         Label.pack()
         Label2 = tk.Label(root, text = 'This application has been created for my final year project', font = ('Comic Sans MS',10))
         Label2.pack()



    def testmic():
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

    file = open("distro.txt")
    data = file.read()
    file.close()

    screensizeout = str(pyautogui.size())


    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("1200x600")
    root.wm_title("Automate It")
    Label = tk.Label(root, text = 'Automate It', font = ('Comic Sans MS',18))
    Label2 = tk.Label(root, text = 'General Functions', font = ('Comic Sans MS',8))
    Label3 = tk.Label(root, text = 'Voice Command', font = ('Comic Sans MS',8))
    Results = tk.Label(root, text = "Your operating system is:" + data, font = ('Comic Sans MS', 12))
    screensize = tk.Label(root, text = "Screen Resolution is:" + screensizeout, font = ('Comic Sans MS', 12))
    button = tk.Button(root, text="Load Email", command=test)
    button2 = tk.Button(root, text="Voice Command", command=ask)
    button3 = tk.Button(root, text="Voice Command 2", command=testmic)
    button4 = tk.Button(root, text="Reset Network", command=netreset)
    button5 = tk.Button(root, text="Empty Bin", command=emptytrash)
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
    Label3.grid(row=0, column=2)
    button2.grid(row=1, column=2)
    button3.grid(row=2, column=2)
    button4.grid(row=2, column=1)
    button5.grid(row=3, column=1)
    status_label = tk.Label(text="")
    status_label.grid(row = 5, column = 1, pady = 50)
    Results.grid(row = 6, column = 1, pady = 330)
    screensize.grid(row = 6, column = 5, pady = 330, padx = 370)
    root.config(menu=menubar)
    root.mainloop()


