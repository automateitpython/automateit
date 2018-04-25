try:
    import pyautogui
    import webbrowser
    import smtplib
    from string import Template
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from tkinter.filedialog import asksaveasfile
    from tkinter.filedialog import askopenfile
    import time
    import re
    import random
    import logging
    import ctypes, sys
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import *
    from tkinter import filedialog
    from PIL import ImageTk, Image
    import speech_recognition as sr
    from time import ctime
    import os
    from gtts import gTTS
    import subprocess
    import PyPDF2
    import distro
    from lxml import html
    import json, requests
    import pyaudio
    import gui
    import automateitcommon
    from PIL import Image
except ImportError:
    raise ImportError('function is not here')


def load():

    urlformail = ""

       
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
    logging.info('Screen Size Detected as'+screensizeout);


    def pass_input(prompt):

        root = tk.Toplevel()
    # this will contain the entered string, and will
    # still exist after the window is destroyed
        var = tk.StringVar()

    # create the GUI
        label = tk.Label(root, text=prompt)
        entry = tk.Entry(root, textvariable=var, show="*")
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

    def email_input(prompt2):

        root = tk.Toplevel()
    # this will contain the entered string, and will
    # still exist after the window is destroyed
        url2 = tk.StringVar()

    # create the GUI
        label2 = tk.Label(root, text=prompt2)
        entry2 = tk.Entry(root, textvariable=url2)
        label2.pack(side="left", padx=(20, 0), pady=20)
        entry2.pack(side="right", fill="x", padx=(0, 20), pady=20, expand=True)

    # Let the user press the return key to destroy the gui 
        entry2.bind("<Return>", lambda event: root.destroy())

    # this will block until the window is destroyed
        root.wait_window()

    # after the window has been destroyed, we can't access
    # the entry widget, but we _can_ access the associated
    # variable
        urlformail = url2.get()
        return urlformail

    def verifiedurl(urlformail2):
        ()
    
    def print_to_gui(text_string):
        status_label.config(text=text_string)
        root.update()


    def imagefinder():
        directory = filedialog.askdirectory()
        for path, dirs, files in os.walk(directory):
            for f in files:
                if f.endswith('.png'):
                    print (os.path.join(path, f))
                if not f.endswith('.png'):
                    print("File Found, but it wasn't an image file")
    
    
    def checkemails():
        while True:
            returned = email_input("Enter Email Address *only @mail.ru and @gmail.com allowed at the moment*")
            if not re.match('[^@]+@[^@]+\.[^@]+', returned):
                print("Please enter a valid email address *only @mail.ru and @gmail.com allowed at the moment")
            else:
                returnedpass = pass_input("Enter password")
                verifiedurl(returned)
                logging.info('Email has been entered correctly as'+returned);
                print(returned)
            break

        
            

        if "mail.ru" in returned:
            def checkmailru():
                if "(1366, 768)" in screensizeout:
                    print("success screensize is correct, using folder 1366x768 for locateonscreen function")
                    mailruinbox = ('1366x768/ruinbox.png')
                webbrowser.open("https://mail.ru")
                logging.info('Mail.ru has been opened, checking to see if user is logged in or not');
                automateitcommon.wait()
                ruinbox = pyautogui.locateCenterOnScreen(mailruinbox)
                if ruinbox is not None:
                    logging.info('User is logged in, opening inbox');
                    pyautogui.click(ruinbox)
                if ruinbox is None:
                    logging.info('User is not logged in, attempting to log user in');
                    automateitcommon.threetab()
                    pyautogui.typewrite(returned)
                    automateitcommon.wait()
                    pyautogui.press('tab')
                    pyautogui.typewrite(returnedpass)
                    automateitcommon.wait()
                pyautogui.press('enter')
            checkmailru()

            
        if "gmail.com" in returned:
            def checkgooglemail():
                if "(1366, 768)" in screensizeout:
                    print("success screensize is correct, using folder 1366x768 for locateonscreen function")
                    gmailloggedin = ('1366x768/gmailalreadyloggedin.png')
                    gmailneedpass = ('1366x768/gmailhi.png')
                    gmailfulllogin = ('1366x768/gmailforgot.png')
                webbrowser.open("https://gmail.com")
                logging.info('Opening Gmail.com in browser');
                gmailalreadyloggedin = pyautogui.locateCenterOnScreen(gmailloggedin)
                if gmailalreadyloggedin is not None:
                    logging.info('User is already logged in, opening inbox');
                    print("You were already logged in, so inbox should be opened by browser")
                gmailhi = pyautogui.locateCenterOnScreen(gmailneedpass)
                if gmailhi is not None:
                    logging.info('User account is presented, but password needed to login, trying to login with password given');
                    pyautogui.typewrite(returnedpass)
                    pyautogui.press('enter')
                gmailforgot = pyautogui.locateCenterOnScreen(gmailfulllogin)
                if gmailforgot is not None:
                    logging.info('User is not logged in, and no stored accout present, attempting full login with details given');
                    print(str(gmailforgot) + "This is gmailforgot")
                    pyautogui.typewrite(returned)
                    pyautogui.press('enter')
                    automateitcommon.wait()
                    pyautogui.typewrite(returnedpass)
                    pyautogui.press('enter')   
            checkgooglemail()
                            

    def speak(audioString):
        print(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save("audio.mp3")
        os.system("wmplayer.exe audio.mp3")

    def recordAudio():
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        data = ""
        WIT_AI_KEY = "4SSPGBBOAN6JTBWKWWELRQ5MONVK67SK"  # Wit.ai keys are 32-character uppercase alphanumeric strings
        try:
            data = r.recognize_wit(audio, key=WIT_AI_KEY)
            print("Witai thinks You Said: " + data)
        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Wit.ai service; {0}".format(e))
        return data
    def jarvis(data):
        if "check weather" in data:
            weather()
            logging.info("User said check weather voice command, opened weather dialog");

        if "check email" in data:
            checkemails()
            logging.info("User said check email voice command, opened email dialog");

        if "reset internet" in data:
            ipconfig()
            logging.info("User said reset internet voice command, resetting internet connection");

        if "set shutdown" in data:
            shutdowntime()
            logging.info("User said set shutdown voice command, opened shutdown dialog");

        if "set restart" in data:
            restarttime()
            logging.info("User said set restart voice command, opened restart dialog");

        if "cancel shutdown" in data:
            cancel()
            logging.info("User said cancel shutdown voice command, cancelled scheduled shutdown");

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
            if "stop" in data:
                speak("Trying to stop voice command")
                return
          

    def shutdowntime():
        shutdowntime = gui_input('Please enter shutdown time in seconds');
        os.system("shutdown /s /t " + shutdowntime);
        logging.info('Shutdown schedule for' + shutdowntime + 'seconds');
    def restarttime():
        restarttime = gui_input('Please enter restart time in seconds');
        os.system("shutdown /r /t " + restarttime );
        logging.info('Restart schedule for' + restarttime + 'seconds'); 
    def cancel():
        os.system("shutdown /a")
        logging.info('Shutdown stopped successfully');
        print_to_gui("Shutdown stopped sucessfully")


    def weather():
        while True:
            location = gui_input("Please input your location")
            r = requests.get('https://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID=04a98ea91424cfbaf5f93095b4be4055')
            data = r.json()
            if r.status_code == 404:
                root = tk.Toplevel()
                Label = tk.Label(root, text = "City not found, please try again", font = ('Comic Sans MS',8))
                Label.pack()
                continue
            else:
                mystring = ""
                mystring = mystring + data['city']['name'] + " "
                mystring = mystring + "Temp:" + str(int(data['list'][0]['main']['temp'] - 273.15)) + "C "
                mystring = mystring + "Max:" + str(int(data['list'][0]['main']['temp_max'] - 273.15)) + "C "
                mystring = mystring + "Min:" + str(int(data['list'][0]['main']['temp_min'] - 273.15)) + "C "
                mystring = mystring + "Hum:" + str(data['list'][0]['main']['humidity']) + "% "
                print (mystring)
                root = tk.Toplevel()
                Label = tk.Label(root, text = mystring, font = ('Comic Sans MS',8))
                Label.pack()
                logging.info(mystring);
            break

    
    def ipconfig():
            command = "ipconfig /release"
            command2 = "ipconfig /renew"# the shell command
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
            process2 = subprocess.Popen(command2, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
            output = process.communicate()
            output2 = process2.communicate()

            print (output[0])
            print (output2[0])

    def fixinternet():
        os.system("route -f")
        os.system("ipconfig /release")
        os.system("ipconfig /renew")
        os.system("arp -d *")
        os.system("nbtstat -R")
        os.system("nbtstat -RR")
        os.system("ipconfig /flushdns")
        os.system("ipconfig /registerdns")

    def customfunction():
        os.system("customfunction1.py")


        

    def joinpdf():
        newdir = filedialog.askdirectory()
        pdfFiles = []
        for filename in os.listdir(newdir):
            if filename.endswith('.pdf'):
                pdfFiles.append(os.path.join(newdir, filename))
        pdfFiles.sort(key = str.lower)
        str1 = ''.join(pdfFiles)
        print("Files found:" + (str1))

        pdfWriter = PyPDF2.PdfFileWriter()

        for filename in pdfFiles:
            pdfFileObj = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            for pageNum in range(1, pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
        savefilename = gui_input("Please enter the name for joined PDF to be saved as:")
        pdfOutput = open(savefilename + ".pdf", 'wb')
        pdfWriter.write(pdfOutput)
        pdfOutput.close()

    def sendemail():
 
        MY_ADDRESS = 'brendan.rodgers@gmail.com'
        PASSWORD = 'vusolo22013'

        def get_contacts(filename):
            names = []
            emails = []
            with open(filename, mode='r', encoding='utf-8') as contacts_file:
                for a_contact in contacts_file:
                    names.append(a_contact.split()[0])
                    emails.append(a_contact.split()[1])
            return names, emails

        def read_template(filename):
 
            with open(filename, 'r', encoding='utf-8') as template_file:
                template_file_content = template_file.read()
            return Template(template_file_content)


        names, emails = get_contacts('emails.txt') # read contacts
        message_template = read_template('message.txt')

    # set up the SMTP server
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
        for name, email in zip(names, emails):
            msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
            message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
            print(message)

        # setup the parameters of the message
            msg['From']=MY_ADDRESS
            msg['To']=email
            msg['Subject']="This is TEST"
        
        # add in the message body
            msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
            s.send_message(msg)
            del msg
        
    # Terminate the SMTP session and close the connection
        s.quit()

    def pingtest():
        while True:
            website = gui_input("Please enter the domain name of the site you would like to check status www." )
            if not re.match('((?:[a-z][a-z\\.\\d\\-]+)\\.(?:[a-z][a-z\\-]+))(?![\\w\\.])', website):
                print("This was not a valid domain, please try again")
            else:
                print("Valid domain name entered, Yay!")
                proc = subprocess.Popen(["ping","www." + website], stdout=subprocess.PIPE, shell=True, encoding='utf8')
                (out, err) = proc.communicate()
                print ("program output:", out)
                root = tk.Tk()
                root.resizable(False, False)
                root.geometry("400x60")
                root.wm_title("Automate It - Website Uptime Check")
                Label = tk.Label(root, text = 'Below is website uptime status', font = ('Comic Sans MS',10))
                Label.pack()
                if "bytes=32" in out:
                    Label2 = tk.Label(root, text = website + '\n' + 'is up and ready to browse', font = ('Comic Sans MS',10), fg="green")
                    Label2.pack()
                else:
                    Label2 = tk.Label(root, text = website + '\n' + 'down, reset your internet or wait for site to go online', font = ('Comic Sans MS',10), fg="red")
                    Label2.pack()
                break

    def deleteUnneeded():
        newdir = filedialog.askdirectory()
        folder = os.path.abspath(newdir)
        for foldername, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                fileSize = os.path.getsize(foldername + '/' + filename)
                folders = os.path.join(folder, filename)
                
                if int(fileSize) < 100:
                    continue

                result = messagebox.askyesno("Found File" + filename, "Are You Sure you want to delete the file" + filename, icon='warning')
                if result == True:
                    os.unlink(folders)
                    print ("Deleted")
                else:
                    print ("Cancelled Deletion")
                #Commented out to protect against accidental deletion

    def websiteip():
        website = gui_input("Please enter the domain name of the site you would like to check status www." )
        process = subprocess.Popen(["nslookup", "www." + website], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8')
        time.sleep(5)
        output = process.communicate()[0].split('\n')
        root = tk.Tk()
        root.resizable(False, False)
        root.geometry("400x180")
        root.wm_title("Automate It - Website Uptime Check")
        Label = tk.Label(root, text = 'Below is the IP that was found for' +'\n' + website, font = ('Comic Sans MS',10))
        Label.pack()

        ip_address=[]

        print(output)
        
        for data in output:
            if 'Addresses:' in data:
                print(data)
                Label2 = tk.Label(root, text = data, font = ('Comic Sans MS',10), fg="green")
                Label2.pack()
            

            if "\t" in data:
                print(data)
                Label2 = tk.Label(root, text = data, font = ('Comic Sans MS',10), fg="green")
                Label2.pack()

    def routerpage():
        process = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8')
        output = process.communicate()[0].split('\n')
        root = tk.Tk()
        root.resizable(False, False)
        root.geometry("400x60")
        root.wm_title("Automate It - Router Page")
        Label = tk.Label(root, text = 'Opening Router Page', font = ('Comic Sans MS',10))
        Label.pack()

        ip_address=[]


        
        for data in output:
            if 'Default Gateway . . . . . . . . . :' in data:
                datafixed= data.replace('Default Gateway . . . . . . . . . : ','')
                print(datafixed)
                urlfix = datafixed.replace(" ", "")
                webbrowser.open("http://"+urlfix)


    def passgenerator():
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

        while True:
            try:
                number = int(gui_input("Please enter the number of passwords you would like to generate (e.g. 2)" ))
            except ValueError:
                print("Not a valid number")
                continue
            else:
                break

        while True:
            try:
                length = int(gui_input("Please enter how long you would like each password to be (e.g. 20)" ))
            except ValueError:
                print("Not a valid number")
                continue
            else:
                break

        print('\nhere are your passwords:')
        with open("generatedpass.txt", "w") as text_file:
            for pwd in range(number):
                password = ''
                for c in range(length):
                    password += random.choice(chars)
                print(password)
           
                text_file.writelines(password+"\n")

    def passwordstrength():
        
        password = gui_input("Please enter the number of passwords you would like to generate (e.g. 2)" )

        def strongPassword(password):

            if passRegex1.search(password) == None:
                return False
            if passRegex2.search(password) == None:
                return False
            if passRegex3.search(password) == None:
                return False
            if passRegex4.search(password) == None:
                return False
            else:
                return True
        
        passRegex1 = re.compile(r'\w{8,}')
        passRegex2 = re.compile(r'\d+')
        passRegex3 = re.compile(r'[a-z]')
        passRegex4 = re.compile(r'[A-Z]')

        root = tk.Tk()
        root.resizable(False, False)
        root.geometry("400x60")
        root.wm_title("Automate It - Password Strength Check")
        

        if strongPassword(password) == True:
            print("Strong Password")
            Label = tk.Label(root, text = 'Password is Strong, Well Done :)', font = ('Comic Sans MS',10), fg="green")
            Label.pack()
        else:
            print("This is not a strong password")
            Label = tk.Label(root, text = 'Password is weak, please do not use this password', font = ('Comic Sans MS',10), fg="red")
            Label.pack()

    def faq():
        print("Hello")

    def createcustomfunction():
        
        filename = None

        def newFile():
            global filename
            filename = "Untitled"
            text.delete(0.0, END)

        def saveFile():
            global filename
            t = text.get(0.0, END)
            f = open(filename, 'w')
            f.write(t)
            f.close()

        def saveAs():
            f = asksaveasfile(defaultextension='.txt')
            t = text.get(0.0, END)
            try:
                f.write(t.rstrip())
            except:
                showerror(title="Oh No!", message="Unable to save file...")

        root = Tk()
        
        def openFile():
            global filename
            file = askopenfile(parent=root,title='Select a File')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()



        root.title("Automate It - Create Custom Function")
        root.minsize(width=400, height=400)
        root.maxsize(width=400, height=400)

        text = Text(root, width=400, height=400)
        text.pack()

        menubar = Menu(root)
        filemenu = Menu(menubar)
        filemenu.add_command(label="New", command=newFile)
        filemenu.add_command(label="Open", command=openFile)
        filemenu.add_command(label="Save", command=saveFile)
        filemenu.add_command(label="Save As", command=saveAs)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        root.config(menu=menubar)
        root.mainloop()
            


    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("700x350")
    root.wm_title("Automate It - Linux Version")
    toolbar = tk.Frame(root)
    toolbar.grid(row=11, column=0, columnspan=2, sticky="w")
    toolbar2 = tk.Frame(root)
    toolbar2.grid(row=11, column=3, columnspan=2, sticky="e")
    Label = tk.Label(root, text = 'Automate It - Windows Version', font = ('Comic Sans MS',18))
    Label2 = tk.Label(text = 'Scheduling Functions', font = ('Comic Sans MS',8))
    Label2.grid(row=0, column=0, pady=5)
    Label3 = tk.Label(text = 'Voice Command', font = ('Comic Sans MS',8))
    Label3.grid(row=0, column=4, pady=5)
    Label4 = tk.Label(text = 'Network Commands', font = ('Comic Sans MS',8))
    Label4.grid(row=0, column=1, pady=5)
    Label5 = tk.Label(text = 'General Functions', font = ('Comic Sans MS',8))
    Label5.grid(row=0, column=2, pady=5)
    Label6 = tk.Label(text = 'Custom Functions', font = ('Comic Sans MS',8))
    Label6.grid(row=0, column=3, pady=5)
    Label7 = tk.Label(text = "Password Functions", font = ('Comic Sans MS', 8))
    Label7.grid(row=6, column=0, pady=5)
    Label8 = tk.Label(text = "File Functions", font = ('Comic Sans MS', 8))
    Label8.grid(row=6, column=1, pady=5)
    status_label = tk.Label(text = "Log")
    Results = tk.Label(toolbar, text="Your operating system is:" + data, font = ('Comic Sans MS', 10))
    Results.grid(row=11, column=0, pady=15)
    screensize = tk.Label(toolbar2, text = "Screen Resolution:" + screensizeout, font = ('Comic Sans MS', 10))
    screensize.grid(row=11, column=3, pady=15)
    status_label.grid(row=10, column=0, pady=20)
    button = tk.Button(text="Timed PC Shutdown", command=shutdowntime)
    button2 = tk.Button(text="Voice Command", command=about)
    button3 = tk.Button(text="Voice Command 2", command=about)
    button4 = tk.Button(text="Timed PC Restart", command=restarttime)              
    button6 = tk.Button(text="Cancel Command", command=cancel)
    button7 = tk.Button(text="Release/Renew IP Address*", command=ipconfig)
    button12 = tk.Button(text="Fix Internet Issues", command=fixinternet)
    button8 = tk.Button(text="Check Weather", command=weather)
    button9 = tk.Button(text="Check Email", command=checkemails)
    button10 = tk.Button(text="Image Check", command=imagefinder)
    button11 = tk.Button(text="Join PDFs", command=joinpdf)
    button13 = tk.Button(text="Custom Function", command=customfunction)
    button14 = tk.Button(text="Send Email", command=sendemail)
    button12 = tk.Button(text="Voice Control", command=ask)
    button16 = tk.Button(text="Check Website Uptime", command=pingtest)
    button17 = tk.Button(text="Delete Big Files", command=deleteUnneeded)
    button18 = tk.Button(text="Website IP Finder", command=websiteip)
    button19 = tk.Button(text="Router Page", command=routerpage)
    button20 = tk.Button(text="Password Generator", command=passgenerator)
    button21 = tk.Button(text="Strength Check", command=passwordstrength)
    button22 = tk.Button(text="Create Function", command=createcustomfunction)
    button.grid(row=1, column=0, padx=10)
    button4.grid(row=2, column=0, padx=10)
    button6.grid(row=3, column=0, padx=10)
    button7.grid(row=1, column=1, padx=10)
    button8.grid(row=1, column=2, padx=10)
    button9.grid(row=2, column=2, padx=10)
    button10.grid(row=8, column=1, padx=10)
    button11.grid(row=9, column=1, padx=10)
    button12.grid(row=1, column=4, padx=10)
    button13.grid(row=1, column=3, padx=10)
    button14.grid(row=3, column=2, padx=10)
    button16.grid(row=2, column=1, padx=10)
    button17.grid(row=7, column=1, padx=10)
    button18.grid(row=3, column=1, padx=10)
    button19.grid(row=4, column=1, padx=10)
    button20.grid(row=7, column=0, padx=10)
    button21.grid(row=8, column=0, padx=10)
    button22.grid(row=2, column=3, padx=10)
    menubar = Menu(root)
    menubar.add_command(label="About", command=about)
    menubar.add_command(label="FAQ", command=faq)
    root.config(menu=menubar)
    root.mainloop()
