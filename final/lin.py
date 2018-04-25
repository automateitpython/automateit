try:
    import pyautogui
    import webbrowser
    import zipfile
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
    from PyPDF2 import PdfFileWriter, PdfFileReader
    import json, requests
    import threading
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
         root.wm_title("Automate It - Linux Version")
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

    # create the dialog
        label = tk.Label(root, text=prompt)
        entry = tk.Entry(root, textvariable=var, show="*")
        label.pack(side="left", padx=(20, 0), pady=20)
        entry.pack(side="right", fill="x", padx=(0, 20), pady=20, expand=True)

    # This lets user press return key to destroy the dialog
        entry.bind("<Return>", lambda event: root.destroy())

    # this will wait until the window is destroyed
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

    # create the dialog
        label = tk.Label(root, text=prompt)
        entry = tk.Entry(root, textvariable=var)
        label.pack(side="left", padx=(20, 0), pady=20)
        entry.pack(side="right", fill="x", padx=(0, 20), pady=20, expand=True)

    # Let the user press the return key to destroy the gui
        entry.bind("<Return>", lambda event: root.destroy())

    # this will wait until the window is destroyed
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

    # create the dialog
        label2 = tk.Label(root, text=prompt2)
        entry2 = tk.Entry(root, textvariable=url2)
        label2.pack(side="left", padx=(20, 0), pady=20)
        entry2.pack(side="right", fill="x", padx=(0, 20), pady=20, expand=True)

    # Let the user press the return key to destroy the gui
        entry2.bind("<Return>", lambda event: root.destroy())

    # this will wait until the window is destroyed
        root.wait_window()

    # after the window has been destroyed, we can't access
    # the entry widget, but we _can_ access the associated
    # variable
        urlformail = url2.get()
        return urlformail

    def verifiedurl(urlformail2): # function needed to pass email string
        ()

    def imageresize(): # function used for resizing image
        directory = filedialog.askdirectory() # open directory dialog
        while True:
            try:
                height = int(gui_input("Please enter height you would like image to be")) # enter new image height
                str(height)
            except ValueError:
                print("Not a valid number")
                continue
            else:
                break
        while True:
            try:
                width = int(gui_input("Please enter width you would like image to be")) # enter new image width
                str(width)
            except ValueError:
                print("Not a valid number")
                continue
            else:
                break
        for file_name in os.listdir(directory):
          print("Processing %s" % file_name)
          image = Image.open(os.path.join(directory, file_name))

          x,y = image.size
          new_dimensions = (int(width), int(height))
          output = image.resize(new_dimensions, Image.ANTIALIAS)
          pngtojpeg = output.convert('RGB')

          output_file_name = os.path.join(directory, "small_" + file_name) # save resized images
          pngtojpeg.save(output_file_name, "JPEG", quality = 95)

        print("All done")


    def imagefinder():
        directory = filedialog.askdirectory() # open directory dialog
        with open("imagecheck.txt", "w") as text_file: # opens image check file ready to save file paths
            for path, dirs, files in os.walk(directory):
                for f in files:
                    if f.endswith('.png'):
                        print(os.path.join(path, f))
                        text_file.writelines(os.path.join(path, f)+"\n")
                    if not f.endswith('.png'):
                        print('File, found, but it was not an image file' +"\n")
                        text_file.writelines("File found but not image" +"\n")

    def filestozip():
        directory = filedialog.askdirectory() # open file dialog
        folder = os.path.abspath(directory)

        number = 1
        while True:
            zipFilename = gui_input("Please enter name for zip file") + '.zip'  # asks for user to input zip file name
            if not os.path.exists(zipFilename):
                break
            number = number + 1

        print('Creating %s...' % (zipFilename))
        backupZip = zipfile.ZipFile(zipFilename, 'w')

        for foldername, subfolders, filenames in os.walk(folder):
            print('Adding files in ' + foldername + '...')
            backupZip.write(foldername)
            for filename in filenames:
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue
                backupZip.write(os.path.join(folder, filename)) # creates zip file

        backupZip.close()
        print('Done')



    def checkemails(): #check emails function
        while True:
            returned = email_input("Enter Email Address *only @mail.ru and @gmail.com allowed at the moment*") # email address input
            if not re.match('[^@]+@[^@]+\.[^@]+', returned):
                print("Please enter a valid email address *only @mail.ru and @gmail.com allowed at the moment") # password input
            else:
                returnedpass = pass_input("Enter password")
                verifiedurl(returned)
                logging.info('Email has been entered correctly as'+returned);
                print(returned)
                break


        cwd = os.getcwd()

        if "mail.ru" in returned:
            def checkmailru(): # function to check mailru email
                if "(1366, 768)" in screensizeout:
                    print(cwd)
                    print("success screensize is correct, using folder 1366x768 for locateonscreen function")
                    mailruinbox = (cwd + '/1366x768/ruinbox.png')
                webbrowser.open("https://e.mail.ru/login?from=mail.login")
                logging.info('Mail.ru has been opened, checking to see if user is logged in or not');
                automateitcommon.wait()
                ruinbox = pyautogui.locateCenterOnScreen(mailruinbox)
                if ruinbox is not None:
                    logging.info('User is logged in, opening inbox');
                    pyautogui.click(ruinbox)
                if ruinbox is None:
                    logging.info('User is not logged in, attempting to log user in');
                    automateitcommon.wait()
                    automateitcommon.wait()
                    pyautogui.typewrite(returned)
                    automateitcommon.wait()
                    automateitcommon.onetab()
                    pyautogui.typewrite(returnedpass)
                    automateitcommon.wait()
                pyautogui.press('enter')
            checkmailru()


        if "gmail.com" in returned:
            def checkgooglemail(): # function to check gmail email
                if "(1366, 768)" in screensizeout:
                    print("success screensize is correct, using folder 1366x768 for locateonscreen function")
                    gmailloggedin = (cwd + '/1366x768//linux/gmailalreadyloggedin.png')
                    gmailneedpass = (cwd +'/1366x768/linux/gmailhi.png')
                    gmailfulllogin = (cwd+ '/1366x768/linux/gmailforgot.png')
                webbrowser.open("https://gmail.com")
                automateitcommon.wait()
                logging.info('Opening Gmail.com in browser');
                gmailalreadyloggedin = pyautogui.locateCenterOnScreen(gmailloggedin)
                if gmailalreadyloggedin is not None:
                    logging.info('User is already logged in, opening inbox');
                    print("You were already logged in, so inbox should be opened by browser")
                gmailhi = pyautogui.locateCenterOnScreen(gmailneedpass)
                if gmailhi is not None:
                    logging.info('User account is presented, but password needed to login, trying to login with password given');
                    print(str(gmailhi) + "This is gmailhi")
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
        tts.save("audio.mp3") # save voice command to audio file to be read by google text to speech
        os.system("mpg123 audio.mp3") # opens the mp3 file to read what was said

    def recordAudio():
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        data = ""
        WIT_AI_KEY = "4SSPGBBOAN6JTBWKWWELRQ5MONVK67SK"  # Wit.ai API Key
            data = r.recognize_wit(audio, key=WIT_AI_KEY)
            print("Witai thinks You Said: " + data)
        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Wit.ai service; {0}".format(e))
        return data
    def voicecommands(data): # function for voice commands, saying each command loads function

        if "website uptime" in data:
            pingtest()
            logging.info("User said check website uptime , opened dialog");

        if "send email" in data:
            sendemail()
            logging.info("User said send email, opened dialog");
            
        if "check image" in data:
            imagefinder()
            logging.info("User said check image, opened  dialog");

        if "join pdf" in data:
            joinpdf()
            logging.info("User said join pdf, opened  dialog");

        if "split pdf" in data:
            splitpdf()
            logging.info("User said split pdf, opened  dialog");

        if "delete files" in data:
            deleteUnneeded()
            logging.info("User said delete files, opened  dialog");

        if "website IP address" in data:
            websiteip()
            logging.info("User said website IP address, opened  dialog");

        if "router" in data:
            routerpage()
            logging.info("User said router page, opened  dialog");

        if "generator" in data:
            passgenerator()
            logging.info("User said password generator, opened dialog");
            
        if "strength" in data:
            passwordstrength()
            logging.info("User said password strength, opened  dialog");
            
        if "change size" in data:
            imageresize()
            logging.info("User said image resize, opened  dialog");
            
        if "zip" in data:
            filestozip()
            logging.info("User said files to zip, opened  dialog");

        if "create function" in data:
            createcustomfunction()
            logging.info("User said create custom function, opened  dialog");

        if "custom function one" in data:
            customfunctionone()
            logging.info("User said custom function one, opened  dialog");

        if "custom function two" in data:
            customfunctionone()
            logging.info("User said custom function two, opened  dialog");

        if "custom function three" in data:
            customfunctionone()
            logging.info("User said custom function three, opened  dialog");

        if "custom function four" in data:
            customfunctionone()
            logging.info("User said custom function four, opened  dialog");

        if "custom function five" in data:
            customfunctionone()
            logging.info("User said custom function five, opened  dialog");
            
        if "check weather" in data:
            weather()
            logging.info("User said check weather voice command, opened weather dialog");

        if "check email" in data:
            checkemails()
            logging.info("User said check email voice command, opened email dialog");

        if "reset internet" in data:
            ipconfig()
            logging.info("User said reset internet voice command, resetting internet connection");

        if "shutdown" in data:
            shutdowntime()
            logging.info("User said set shutdown voice command, opened shutdown dialog");

        if "restart" in data:
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
        def callback(): # uses threading for voice so GUI doesnt freeze
            time.sleep(2)
            speak("Hi, what can I do for you?")
            while 1:
                data = recordAudio()
                voicecommands(data)
                if "stop" in data:
                    speak("Trying to stop voice command")
                    return
        t = threading.Thread(target=callback)
        t.start()
        


     def shutdowntime():  # shutdown schedule function
        while True:
            try:
                shutdowntime = int(gui_input('Please enter shutdown time in minutes'));
                str(shutdowntime)
            except ValueError:
                print("Not a valid number")
                continue
            else:
                break
        process = subprocess.Popen(["shutdown", str(shutdowntime)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8')
        print(process)
        time.sleep(5)
        output = process.communicate()[0].split('\n')
        root = tk.Tk()
        root.resizable(False, False)
        root.geometry("400x180")
        root.wm_title("Automate It - Shutdown Schedule Dialog")
        Label = tk.Label(root, font = ('Comic Sans MS',10))
        Label.pack()


        print(output)

        for data in output:
            if 'Shutdown' in data:
                print(data)
                datafixed= data.replace("use 'shutdown -c' to cancel.",'')
                Label2 = tk.Label(root, text = datafixed, font = ('Comic Sans MS',10), fg="green")
                Label2.pack()
                logging.info(datafixed);
    def restarttime(): # restart schedule function
        while True:
            try:
                restarttime = int(gui_input('Please enter restart time in minutes'));
                str(restarttime)
            except ValueError:
                print("Not a valid number")
                continue
            else:
                break

        print(restarttime)
        process = subprocess.Popen(["shutdown", "-r", str(restarttime)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8')
        print(process)
        time.sleep(5)
        output = process.communicate()[0].split('\n')
        root = tk.Tk()
        root.resizable(False, False)
        root.geometry("400x180")
        root.wm_title("Automate It - Website Uptime Check")
        Label = tk.Label(root, font = ('Comic Sans MS',10))
        Label.pack()


        print(output)

        for data in output:
            if 'Shutdown' in data:
                print(data)
                datafixed= data.replace("use 'shutdown -c' to cancel.",'')
                datafixed2=datafixed.replace("Shutdown","Restart")
                Label2 = tk.Label(root, text = datafixed2, font = ('Comic Sans MS',10), fg="green")
                Label2.pack()
                logging.info(datafixed2);
    def cancel(): # cancel schedule shutdown or restart
        os.system("shutdown -c")
        root = tk.Tk()
        root.resizable(False, False)
        root.geometry("400x80")
        root.wm_title("Automate It - Website Uptime Check")
        Label = tk.Label(root, text="Shutdown schedule purged", font = ('Comic Sans MS',10), fg="green")
        Label.pack()
        logging.info('Shutdown schedule purged');

    def weather(): # check weather function
        while True:
            location = gui_input("Please input your location") # allow user to input location
            if not re.match("^[a-z]*$", location):
                print("Only letters are allowed in weather location")
            else:
                r = requests.get('https://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID=04a98ea91424cfbaf5f93095b4be4055') # connect to API gather weather data
                data = r.json()
                if r.status_code == 404: # if error is displayed when wrong entered
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
                    logging.info("Weather data found" + mystring);
                break
            

     def ipconfig(): #  restart internet
            command = "systemctl restart NetworkManager.service"
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
            output = process.communicate()

            print (output[0])



    def customfunctionone():
        os.system(" python customfunction1.py")
		logging.info('Custom Function One Loaded');

    def customfunctiontwo():
        os.system(" python customfunction2.py")
		logging.info('Custom Function Two Loaded');

    def customfunctionthree():
        os.system(" python customfunction3.py")
		logging.info('Custom Function Three Loaded');

    def customfunctionfour():
        os.system(" python customfunction4.py")
		logging.info('Custom Function Four loaded');

    def customfunctionfive():
        os.system(" python customfunction5.py")
		logging.info('Custom Function Five Loaded');




    def joinpdf(): # join pdf function 
        newdir = filedialog.askdirectory() # open directory dialog
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
        savefilename = gui_input("Please enter the name for joined PDF to be saved as:") # prompt user for new pdf file name
        pdfOutput = open(savefilename + ".pdf", 'wb')
        pdfWriter.write(pdfOutput)
        pdfOutput.close()
		logging.info('PDF Files Joined');
		

    def splitpdf(): # split pdf function

        pdffile =  filedialog.askopenfilename(initialdir="/home", title = "Select pdf file to split",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
        directory = filedialog.askdirectory() # open file dialog
        inputpdf = PdfFileReader(open(pdffile, "rb"))

        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open(directory+"/document-page%s.pdf" % i, "wb") as outputStream:
                output.write(outputStream)
			logging.info('PDF File Split');


    def sendemail(): # send email function
        while True:
            myemail = gui_input("Enter Email Address *only @mail.ru and @gmail.com allowed at the moment*") # prompt user to enter email address
            if not re.match('[^@]+@[^@]+\.[^@]+', myemail):
                print("Please enter a valid email address *only @mail.ru and @gmail.com allowed at the moment")
            else:
                password = pass_input("Enter password") # prompt user to enter password
                logging.info('Email has been entered correctly as'+myemail);
                print(myemail)
                break


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

        emailfile =  filedialog.askopenfilename(initialdir="/home", title = "Select text file containing emails",filetypes = (("txt files","*.txt"),("all files","*.*")))
        print (emailfile)
        names, emails = get_contacts(emailfile) # read contacts
        messagefile =  filedialog.askopenfilename(initialdir = "/home",title = "Select text fie containing message to be sent",filetypes = (("txt files","*.txt"),("all files","*.*")))
        print (messagefile)
        message_template = read_template(messagefile)

    # set up the SMTP server
        smtpserver =gui_input("Please enter SMTP Sever")
        s = smtplib.SMTP(host=smtpserver, port=587)
        s.starttls()
        s.login(myemail, password)


    # For each contact, send the email:
        subject=gui_input("Please enter subject for email")
        root = tk.Tk()
        root.resizable(False, False)
        root.geometry("400x120")
        root.wm_title("Automate It - Email Send Check")
        for name, email in zip(names, emails):
            msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
            message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
            print(message)

            Label = tk.Label(root, text="Emails have been sent to" +":" + email, font = ('Comic Sans MS',10), fg="green")
            Label.pack()
            logging.info('Emails sent');


        # setup the parameters of the message
            msg['From']=myemail
            msg['To']=email
            msg['Subject']=subject

        # add in the message body
            msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
            s.send_message(msg)
            del msg

    # Terminate the SMTP session and close the connection
        s.quit()
		logging.info('Emails Sent');

  os.system(" python customfunction4.py")

    def deleteUnneeded(): # delete files function 
        maxfilesize = gui_input("Up to What File Size would you like to delete files (in MBytes)") # enter max file size of files below size to be deleted
        newdir = filedialog.askdirectory()
        folder = os.path.abspath(newdir)
        for foldername, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                fileSize = os.path.getsize(foldername + '/' + filename)>> 20
                folders = os.path.join(folder, filename)

                if int(fileSize) < int(maxfilesize):
                    continue

                result = messagebox.askyesno("Found File" + filename, "Are You Sure you want to delete the file" + filename, icon='warning')
                if result == True:
                    os.unlink(folders)
                    print ("Deleted")
					logging.info('File Deleted');
                else:
                    print ("Cancelled Deletion")
					logging.info('Deletion Cancelled');
                #Commented out to protect against accidental deletion

    def websiteip(): # website ip check function
        while True:
            website = gui_input("Please enter the domain name of the site you would like to check status www." )
            if not re.match('((?:[a-z][a-z\\.\\d\\-]+)\\.(?:[a-z][a-z\\-]+))(?![\\w\\.])', website):
                print("This was not a valid domain, please try again")
            else:
                process = subprocess.Popen(["host", "www." + website], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8')
                print(process)
                time.sleep(5)
                output = process.communicate()[0].split('\n')
                root = tk.Tk()
                root.resizable(False, False)
                root.geometry("400x200")
                root.wm_title("Automate It - Website Uptime Check")
                Label = tk.Label(root, text = 'Below is the IP that was found for' +'\n' + website, font = ('Comic Sans MS',10))
                Label.pack()


                print(output)

                for data in output:
                    if 'has address' in data:
                        print(data)
                        Label2 = tk.Label(root, text = data, font = ('Comic Sans MS',10), fg="green")
                        Label2.pack()
                break


    def routerpage(): #  open router page function
        process = subprocess.Popen(["ip", "route", "show"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8')
        output = process.communicate()[0].split('\n')
        root = tk.Tk()
        root.resizable(False, False)
        root.geometry("400x60")
        root.wm_title("Automate It - Router Page")
        Label = tk.Label(root, text = 'Opening Router Page', font = ('Comic Sans MS',10))
        Label.pack()

    def passgenerator(): # password generator function
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

        while True:
            try:
                number = int(gui_input("Please enter the number of passwords you would like to generate (e.g. 2)" )) # prompts user for number of passwords
            except ValueError:
                print("Not a valid number")
                continue
            else:
                break

        while True:
            try:
                length = int(gui_input("Please enter how long you would like each password to be (e.g. 20)" )) # prompts user for length of passwords
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

                text_file.writelines(password+"\n") # write passwords to generatepass.txt file
		logging.info('Passwords generated and saved to generatedpass.txt');

    def passwordstrength(): # password strength check function 

        password = gui_input("Please enter the number of passwords you would like to generate (e.g. 2)" ) # prompts user to enter password

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
			logging.info('Password entered was strong');
        else:
            print("This is not a strong password")
            Label = tk.Label(root, text = 'Password is weak, please do not use this password', font = ('Comic Sans MS',10), fg="red")
            Label.pack()
			logging.info('Password entered was weak');

    def faq(): # faq help function
        filename = None
        root = Tk()

        cwd = os.getcwd()


        def openschedule():
            global filename
            file = open(cwd+'/help/schedule.txt', 'r')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()

        def opennetwork():
            global filename
            file = open(cwd+'/help/network.txt', 'r')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()

        def opengeneral():
            global filename
            file = open(cwd+'/help/general.txt', 'r')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()

        def openvoice():
            global filename
            file = open(cwd+'/help/voice.txt', 'r')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()

        def openpassword():
            global filename
            file = open(cwd+'/help/pass.txt', 'r')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()

        def openfile():
            global filename
            file = open(cwd+'/help/file.txt', 'r')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()





# GUI code below for help topics/faq window

        root.title("Automate It - Help Topics")
        root.minsize(width=400, height=400)
        root.maxsize(width=400, height=400)

        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)

        text = Text(root, width=400, height=400,wrap=WORD, yscrollcommand=scrollbar.set)
        text.pack()

        scrollbar.config(command=text.yview)

        menubar = Menu(root)
        helpmenu = Menu(menubar)
        filemenu = Menu(menubar)
        filemenu.add_command(label="Quit", command=root.quit)
        menubar.add_cascade(label="Quit", menu=filemenu)
        menubar.add_cascade(label="Help Topics", menu=helpmenu)
        helpmenu.add_command(label="Scheduling Function Help", command=openschedule)
        helpmenu.add_command(label="Network Function Help", command=opennetwork)
        helpmenu.add_command(label="General Function Help", command=opengeneral)
        helpmenu.add_command(label="Voice Control Help", command=openvoice)
        helpmenu.add_command(label="Password Function Help", command=openpassword)
        helpmenu.add_command(label="File Function Help", command=openfile)

        root.config(menu=menubar)
        root.mainloop()


    def createcustomfunction(): # create custom function function

        filename = None

        root = Tk()

        def savecustomone():
            file = open('customfunction1.py','w')
            t = text.get(0.0, END)
            try:
                file.write(t.rstrip())
            except:
                showerror(title="Oh No!", message="Unable to save file...")

        def savecustomtwo():
            file = open('customfunction2.py','w')
            t = text.get(0.0, END)
            try:
                file.write(t.rstrip())
            except:
                showerror(title="Oh No!", message="Unable to save file...")

        def savecustomthree():
            file = open('customfunction3.py','w')
            t = text.get(0.0, END)
            try:
                file.write(t.rstrip())
            except:
                showerror(title="Oh No!", message="Unable to save file...")

        def savecustomfour():
            file = open('customfunction4.py','w')
            t = text.get(0.0, END)
            try:
                file.write(t.rstrip())
            except:
                showerror(title="Oh No!", message="Unable to save file...")

        def savecustomfive():
            file = open('customfunction5.py','w')
            t = text.get(0.0, END)
            try:
                file.write(t.rstrip())
            except:
                showerror(title="Oh No!", message="Unable to save file...")

        def opencustomone():
            global filename
            file = open('customfunction1.py', 'r')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()

        def opencustomtwo():
            global filename
            file = open('customfunction2.py', 'w')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()

        def opencustomthree():
            global filename
            file = open('customfunction3.py', 'w')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()

        def opencustomfour():
            global filename
            file = open('customfunction4.py', 'w')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()

        def opencustomfive():
            global filename
            file = open('customfunction5.py', 'w')
            filename = file.name
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
            file.close()

# GUI code for Create Custom Function dialog
        root.title("Automate It - Create Custom Function")
        root.minsize(width=400, height=400)
        root.maxsize(width=400, height=400)

        text = Text(root, width=400, height=400)
        text.pack()

        menubar = Menu(root)
        savemenu = Menu(menubar)
        filemenu = Menu(menubar)
        loadmenu = Menu(menubar)
        filemenu.add_command(label="Quit", command=root.quit)
        menubar.add_cascade(label="Quit", menu=filemenu)
        menubar.add_cascade(label="Save Menu", menu=savemenu)
        savemenu.add_command(label="Save Function 1", command=savecustomone)
        savemenu.add_command(label="Save Function 2", command=savecustomtwo)
        savemenu.add_command(label="Save Function 3", command=savecustomthree)
        savemenu.add_command(label="Save Function 4", command=savecustomfour)
        savemenu.add_command(label="Save Function 5", command=savecustomfive)
        menubar.add_cascade(label="Load Menu", menu=loadmenu)
        loadmenu.add_command(label="Load Function 1", command=opencustomone)
        loadmenu.add_command(label="Load Function 2", command=opencustomtwo)
        loadmenu.add_command(label="Load Function 3", command=opencustomthree)
        loadmenu.add_command(label="Load Function 4", command=opencustomfour)
        loadmenu.add_command(label="Load Function 5", command=opencustomfive)

        root.config(menu=menubar)
        root.mainloop()


# Main GUI Code

    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("810x370")
    root.wm_title("Automate It - Linux Version")
    toolbar = tk.Frame(root)
    toolbar.grid(row=11, column=0, columnspan=2, sticky="w")
    toolbar2 = tk.Frame(root)
    toolbar2.grid(row=11, column=4, columnspan=2, sticky="e")
    Label = tk.Label(root, text = 'Automate It - Linux Version', font = ('Comic Sans MS',18))
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
    Label9 = tk.Label(text = "Image Functions", font = ('Comic Sans MS', 8))
    Label9.grid(row=6, column=2, pady=5)
    Results = tk.Label(toolbar, text="Your operating system is:" + data, font = ('Comic Sans MS', 10))
    Results.grid(row=11, column=0, pady=50)
    screensize = tk.Label(toolbar2, text = "Screen Resolution:" + screensizeout, font = ('Comic Sans MS', 10))
    screensize.grid(row=11, column=5, pady=25)
    timedshutdown = tk.Button(text="Timed PC Shutdown", command=shutdowntime)
    timedrestart = tk.Button(text="Timed PC Restart", command=restarttime)
    cancelcommand = tk.Button(text="Cancel Command", command=cancel)
    resetinternet = tk.Button(text="Release/Renew IP Address*", command=ipconfig)
    checkweather = tk.Button(text="Check Weather", command=weather)
    checkemail = tk.Button(text="Check Email", command=checkemails)
    imagecheck = tk.Button(text="Image Check", command=imagefinder)
    joinpdffile = tk.Button(text="Join PDFs", command=joinpdf)
    customfunction1 = tk.Button(text="Custom Function 1", command=customfunctionone)
    sendemails = tk.Button(text="Send Email", command=sendemail)
    voicecontrol = tk.Button(text="Voice Control", command=ask)
    checksite = tk.Button(text="Check Website Uptime", command=pingtest)
    deletefiles = tk.Button(text="Delete Files", command=deleteUnneeded)
    websiteipcheck = tk.Button(text="Website IP Finder", command=websiteip)
    routerpagecheck = tk.Button(text="Router Page", command=routerpage)
    passwordgenerator = tk.Button(text="Password Generator", command=passgenerator)
    passstrength = tk.Button(text="Strength Check", command=passwordstrength)
    createfunction = tk.Button(text="Create Function", command=createcustomfunction)
    customfunction2 = tk.Button(text="Custom Function 2", command=customfunctiontwo)
    customfunction3 = tk.Button(text="Custom Function 3", command=customfunctionthree)
    customfunction4 = tk.Button(text="Custom Function 4", command=customfunctionfour)
    customfunction5 = tk.Button(text="Custom Function 5", command=customfunctionfive)
    splitpdffile = tk.Button(text="Split PDF", command=splitpdf)
    imageresizer = tk.Button(text="Image Resize", command=imageresize)
    filestozipfile = tk.Button(text="Files to Zip", command=filestozip)
    timedshutdown.grid(row=1, column=0)
    timedrestart.grid(row=2, column=0)
    cancelcommand.grid(row=3, column=0)
    resetinternet.grid(row=1, column=1)
    checkweather.grid(row=1, column=2)
    checkemail.grid(row=2, column=2)
    imagecheck.grid(row=8, column=2)
    joinpdffile.grid(row=9, column=1)
    voicecontrol.grid(row=1, column=4, padx=10)
    customfunction1.grid(row=1, column=3)
    sendemails.grid(row=3, column=2)
    checksite.grid(row=2, column=1)
    deletefiles.grid(row=7, column=1)
    websiteipcheck.grid(row=3, column=1)
    routerpagecheck.grid(row=4, column=1)
    passwordgenerator.grid(row=7, column=0)
    passstrength.grid(row=8, column=0)
    createfunction.grid(row=6, column=3, padx=40)
    customfunction2.grid(row=2, column=3, padx=40)
    customfunction3.grid(row=3, column=3, padx=40)
    customfunction4.grid(row=4, column=3, padx=40)
    customfunction5.grid(row=5, column=3, padx=40)
    splitpdffile.grid(row=10, column=1)
    imageresizer.grid(row=7, column=2)
    filestozipfile.grid(row=8, column=1)
    menubar = Menu(root)
    menubar.add_command(label="About", command=about)
    menubar.add_command(label="FAQ", command=faq)
    root.config(menu=menubar)
    root.mainloop()
