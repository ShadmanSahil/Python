from tkinter import *
import os
import PyPDF2
import random
import string
import speech_recognition as sr
import pyttsx3

def generate_password():
    global y
    password = []
    for i in range(4):
        alpha = random.choice(string.ascii_letters)
        number = random.choice(string.digits)
        password.append(alpha)
        password.append(number)
    y = "".join(str(x) for x in password)


def locked():
    global stored
    stored = directory.get()
    directory.delete(0, END)

    pdfFile = open(stored, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    generate_password()
    password2 = y

    file5 = open("Locked_Files.txt", "a")
    file5.write(stored + " ")
    file5.write(password2 + "\n")
    file5.close()

    pdfWriter.encrypt(password2)
    new_name = stored + "_Locked.pdf"
    resultPdf = open(new_name, 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
    pdfFile.close()
    os.remove(stored)

    screen8.destroy()
    global screen9
    screen9 = Tk()
    screen9.geometry("300x200")
    Label(screen9, text="File has been locked").pack()
    Label(screen9, text="").pack()
    Button(screen9, text="Ok", command=delete9).pack()


def delete9():
    screen9.destroy()


def lock():
    global directory
    screen7.destroy()
    global screen8
    screen8 = Tk()
    screen8.geometry("300x200")
    Label(screen8, text="Please enter the file directory").pack()
    directory = Entry(screen8)
    directory.pack()
    Button(screen8, text="Lock", command=locked).pack()


def delete4():
    global screen7
    screen4.destroy()
    screen7 = Tk()
    screen7.geometry("300x250")
    Label(screen7, text="Select a task").pack()
    Label(screen7, text="").pack()
    Button(screen7, text="Lock a file", command=lock).pack()
    Label(screen7, text="").pack()
    Button(screen7, text="Unlock a file", command=unlock).pack()


def unlock():
    screen7.destroy()
    global screen10
    global directory_unlock
    screen10 = Tk()
    screen10.geometry("300x200")
    Label(screen10, text="Please enter the file directory").pack()
    directory_unlock = Entry(screen10)
    directory_unlock.pack()
    Button(screen10, text="Get Password", command=show_password).pack()


def show_password():
    your_file = directory_unlock.get()
    screen10.destroy()
    screen11 = Tk()
    screen11.geometry("300x200")
    Label(screen11, text="Here is the password").pack()
    file = open('C:/Users/Sharfuddin/Desktop/Project/Locked_Files.txt', 'r')
    read = file.readlines()
    x = ''
    for line in read:
        if your_file in line:
            x = str(line)
            x = x.split(' ')
    print(x[1])


def delete5():
    screen5.destroy()


def delete6():
    screen6.destroy()


def user_not_found():
    global screen6
    screen6 = Toplevel(screen3)
    screen6.geometry("150x100")
    Label(screen6, text="User Not Found!", fg="red").pack()
    Label(screen6, text="Please Re-enter").pack()
    Button(screen6, text="OK", command=delete6).pack()


def login_success():
    screen3.destroy()
    global screen4
    screen4 = Tk()
    screen4.geometry("150x100")
    Label(screen4, text="Login Successful", fg="green").pack()
    Button(screen4, text="OK", command=delete4).pack()


def incorrect_password():
    global screen5
    screen5 = Toplevel(screen3)
    screen5.geometry("150x100")
    Label(screen5, text="Incorrect Password!", fg="red").pack()
    Label(screen5, text="Please Re-enter").pack()
    Button(screen5, text="OK", command=delete5).pack()


def login_user():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    x = GUI_d(username1, password1)
    x.new()


def register_user():
    global username_info
    global password_info
    username_info = username.get()
    password_info = password.get()

    x = GUI_e(username_info, password_info)
    x.new()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    screen1.destroy()
    global screen2
    screen2 = Tk()
    screen2.geometry("250x150")
    Label(screen2, text="Registration Successful", fg="green").pack()
    Button(screen2, text="Ok", command=register_success).pack()


def register_success():
    screen2.destroy()


def register():
    global screen1
    screen.destroy()
    screen1 = Tk()
    screen1.geometry("300x250")
    screen1.title("Sign-Up Form")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter your details").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width="10", height="1", command=register_user).pack()


def login():
    screen.destroy()
    global screen3
    screen3 = Tk()
    screen3.title("Login Page")
    screen3.geometry("300x250")

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen3, text="Please enter your details to login").pack()
    Label(screen3, text="").pack()
    username_entry1 = Entry(screen3, textvariable=username_verify)
    username_entry1.pack()
    Label(screen3, text="Password").pack()
    password_entry1 = Entry(screen3, textvariable=password_verify)
    password_entry1.pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Login", width="10", height="1", command=login_user).pack()


def window():
    global screen
    screen = Tk()
    screen.geometry("300x150")
    screen.title("Home Page")
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


def windowYes():
    speaker.say("Do you want to login or register?")
    speaker.runAndWait()
    speaker.stop()
    with sr.Microphone() as source:
        speaker.say("Speak now: ")
        speaker.runAndWait()
        speaker.stop()
        print("Speak now: ")
        audio = speech.listen(source)
        try:
            text = speech.recognize_google(audio)
            print(text)

        except:
            speaker.say("Sorry could not recognize your voice. ")
            speaker.runAndWait()
            speaker.stop()
            print("Sorry could not recognize your voice. ")
        if "register" in text:
            speaker.say("Say your username. ")
            speaker.runAndWait()
            speaker.stop()
            print("Say your username: ")
            audio = speech.listen(source)
            try:
                username_info = speech.recognize_google(audio)
                print(username_info)
            except:
                print("Sorry could not recognize your voice. ")
            speaker.say("Say the password. ")
            speaker.runAndWait()
            speaker.stop()
            print("Say the password: ")
            audio = speech.listen(source)
            try:
                password_info = speech.recognize_google(audio)
                print(password_info)
            except:
                speaker.say("Sorry could not recognize your voice. ")
                speaker.runAndWait()
                speaker.stop()
                print("Sorry could not recognize your voice. ")
            x = GUI_e(username_info, password_info)
            x.new()
            speaker.say("Your registration is successful!")
            speaker.runAndWait()
            speaker.stop()
            print("Registration successful!")
        elif "log in" in text:
            speaker.say("Say your username. ")
            speaker.runAndWait()
            speaker.stop()
            print("Say your username: ")
            audio = speech.listen(source)
            try:
                username_info = speech.recognize_google(audio)
                print(username_info)
            except:
                print("Sorry could not recognize your voice. ")
            speaker.say("Say the password. ")
            speaker.runAndWait()
            speaker.stop()
            print("Say the password: ")
            audio = speech.listen(source)
            try:
                password_info = speech.recognize_google(audio)
                print(password_info)
            except:
                speaker.say("Sorry could not recognize your voice. ")
                speaker.runAndWait()
                speaker.stop()
                print("Sorry could not recognize your voice. ")
            x = GUI_d(username_info, password_info)
            x.new()
            speaker.say("Your log in is successful!")
            speaker.runAndWait()
            speaker.stop()
            print("Login successful!")


speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
voices = speaker.getProperty('rate')
speaker.setProperty('rate', 150)
voices = speaker.getProperty('volume')
speaker.setProperty('volume', 1.0)
speaker.say("Do you want to use our speech recognition feature? Please say Yes or No.")
speaker.runAndWait()
speaker.stop()

speech = sr.Recognizer()

with sr.Microphone() as source:
    speaker.say("Speak now: ")
    speaker.runAndWait()
    speaker.stop()
    print("Speak now: ")
    audio = speech.listen(source)

    try:
        text = speech.recognize_google(audio)
        print(text)

    except:
        print("Sorry could not recognize your voice. ")

if "yes" in text:
    windowYes()
elif "no" in text:
    window()
