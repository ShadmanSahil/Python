from tkinter import *
import os
import PyPDF2
import random
import string
import speech_recognition as sr
import pyttsx3


class GUI_d:
    def __init__(self, username, password):
        self.name = username
        self.Pass = password

    def caesar(self, word, dir, n):
        x = list(word)
        a = 'abcdefghijklmnopqrstuvwxyz'
        b = a.upper()
        a = list(a)
        b = list(b)
        if dir == 'l':
            if n == 'brute':
                for i in range(1, 27):
                    am = []
                    c = a[-i:] + a[:-i]
                    d = b[-i:] + b[:-i]
                    for k in range(len(x)):
                        if x[k] in a:
                            am.append(c[a.index(x[k])])
                        elif x[k] in b:
                            am.append(d[b.index(x[k])])
                        else:
                            am.append(x[k])
                    z = str(i)
                    print('Left Shift of ' + z, ':', ''.join(am))
            else:
                n = int(n)
                c = a[-n:] + a[:-n]
                d = b[-n:] + b[:-n]
                for k in range(len(x)):
                    if x[k] in a:
                        x[k] = c[a.index(x[k])]
                    elif x[k] in b:
                        x[k] = d[b.index(x[k])]
                return ''.join(x)
        elif dir == 'r':
            if n == 'brute':
                for i in range(1, 27):
                    am = []
                    c = a[i:] + a[:i]
                    d = b[i:] + b[:i]
                    for k in range(len(x)):
                        if x[k] in a:
                            am.append(c[a.index(x[k])])
                        elif x[k] in b:
                            am.append(d[b.index(x[k])])
                        else:
                            am.append(x[k])
                    z = str(i)
                    print('Righ Shift of ' + z, ':', ''.join(am))
            else:
                n = int(n)
                c = a[n:] + a[:n]
                d = b[n:] + b[:n]
                for k in range(len(x)):
                    if x[k] in a:
                        x[k] = c[a.index(x[k])]
                    elif x[k] in b:
                        x[k] = d[b.index(x[k])]
                return ''.join(x)

    def vigenere(self, word1, key1):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        alpha = list(alpha)
        gamma = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        gamma = list(gamma)
        word = list(word1)
        key = list(key1)
        # keeping record of index position of alphabets in key
        x = []
        for z in range(len(key)):
            if key[z] in alpha:
                x.append(alpha.index(key[z]))
            elif key[z] in gamma:
                x.append(gamma.index(key[z]))
        # keeping record of index position of spaces
        a = []
        for c in range(len(word)):
            if word[c] == ' ':
                a.append(c)
        # removing all spaces
        while word.count(' ') != 0:
            word.remove(' ')
        # encrypting using vigenere cipher
        for i in range(len(x)):
            for k in range(i, len(word), len(x)):
                if word[k] in alpha:
                    n = alpha.index(word[k])
                    if n - x[i] < 0:
                        beta = alpha[n + 1:] + alpha[:n + 1]
                        word[k] = beta[beta.index(word[k]) - x[i]]
                    else:
                        word[k] = alpha[n - x[i]]
                elif word[k] in gamma:
                    n = gamma.index(word[k])
                    if n - x[i] < 0:
                        beta = gamma[n + 1:] + gamma[:n + 1]
                        word[k] = beta[beta.index(word[k]) - x[i]]
                    else:
                        word[k] = gamma[n - x[i]]
        # adding spaces in original position
        new = []
        for j in range(len(word)):
            if j in a:
                new.insert(j, ' ')
            new.append(word[j])
        return ''.join(new)

    def rsaAlgorithmD(self, t, p, q):
        def gcd(ele1, ele2):
            if ele2 == 0:
                return ele1
            else:
                return gcd(ele2, ele1 % ele2)

        p = int(p)
        q = int(q)
        text = ""
        N = p * q
        phiN = (p - 1) * (q - 1)
        for i in range(2, phiN):
            if gcd(N, i) == 1 and gcd(phiN, i) == 1:
                e = i
                break
        k = 1
        d = (phiN * k + 1) / e
        while d != int(d):
            k += 1
            d = (phiN * k + 1) / e
        t = t.split(' ')
        i = 0
        for j in range(len(t)):
            if t[j].isnumeric() and i == 0:
                t[j] = int(t[j])
                calc = 64 + int((t[j] ** d) % N)
                text += chr(calc)
                i += 1
            elif t[j].isnumeric():
                t[j] = int(t[j])
                calc = 96 + int((t[j] ** d) % N)
                text += chr(calc)
            elif j != (len(t) - 1) and t[j] == '' and t[j + 1] == '':
                text += ' '
            else:
                text += t[j]
        return text

    def new(self):
        file = open('file-1.txt', 'r')
        read = file.readlines()
        x = ''
        c = []
        a = []
        for line in read:
            if str(self.name) in line:
                x = str(line)
                x = x.split(' ')
                a.append('y')
                c.append(x)
            else:
                a.append('n')
        if 'y' not in a:
            user_not_found()
            return 'Username not found'
        else:
            z = []
            for k in range(len(c)):
                pa = (c[k])[1]
                if len(pa) == len(self.Pass):
                    z = c[k]
            if z != []:
                password = z[1]
                new = z[2:]
                for i in range(len(new) - 1, -1, -1):
                    if new[i] == 'caesar':
                        if new[i + 1] == 'r':
                            password = self.caesar(password, 'l', new[i + 2])
                        elif new[i + 1] == 'l':
                            password = self.caesar(password, 'r', new[i + 2])
                    elif new[i] == 'vig':
                        password = self.vigenere(password, new[i + 1])
                    elif new[i] == 'rsa':
                        password = self.rsaAlgorithmD(password, new[i + 1], new[i + 2])
                if self.Pass == password:
                    login_success()
                    return 'correct password'
                else:
                    incorrect_password()
                    return 'wrong password'

            else:
                incorrect_password()
                return 'wrong password'


class GUI_e:

    def __init__(self, username, password):
        self.name = username
        self.Pass = password
        self.types = ['caesar', 'vig', 'rsa']
        self.n = len(self.Pass)

    def caesar(self, word, dir, n):
        x = list(word)
        a = 'abcdefghijklmnopqrstuvwxyz'
        b = a.upper()
        a = list(a)
        b = list(b)
        if dir == 'l':
            if n == 'brute':
                # speaker.say('performing brute force encryption with left shift')
                # speaker.runAndWait()
                for i in range(1, 27):
                    am = []
                    c = a[-i:] + a[:-i]
                    d = b[-i:] + b[:-i]
                    for k in range(len(x)):
                        if x[k] in a:
                            am.append(c[a.index(x[k])])
                        elif x[k] in b:
                            am.append(d[b.index(x[k])])
                        else:
                            am.append(x[k])
                    z = str(i)
                    print('Left Shift of ' + z, ':', ''.join(am))
            else:
                # speaker.say('performing caesar cipher encryption with left shift of {}'.format(int(n)))
                # speaker.runAndWait()
                n = int(n)
                c = a[-n:] + a[:-n]
                d = b[-n:] + b[:-n]
                for k in range(len(x)):
                    if x[k] in a:
                        x[k] = c[a.index(x[k])]
                    elif x[k] in b:
                        x[k] = d[b.index(x[k])]
                return ''.join(x)
                # speaker.say('encryption complete')
                # speaker.runAndWait()
        elif dir == 'r':
            if n == 'brute':
                # speaker.say('performing brute force encryption with right shift')
                # speaker.runAndWait()
                for i in range(1, 27):
                    am = []
                    c = a[i:] + a[:i]
                    d = b[i:] + b[:i]
                    for k in range(len(x)):
                        if x[k] in a:
                            am.append(c[a.index(x[k])])
                        elif x[k] in b:
                            am.append(d[b.index(x[k])])
                        else:
                            am.append(x[k])
                    z = str(i)
                    print('Righ Shift of ' + z, ':', ''.join(am))
            else:
                # speaker.say('performing caesar cipher encryption with right shift of {}'.format(int(n)))
                # speaker.runAndWait()
                n = int(n)
                c = a[n:] + a[:n]
                d = b[n:] + b[:n]
                for k in range(len(x)):
                    if x[k] in a:
                        x[k] = c[a.index(x[k])]
                    elif x[k] in b:
                        x[k] = d[b.index(x[k])]
                return ''.join(x)
                # speaker.say('encryption complete')
                # speaker.runAndWait()

    def vigenere(self, word, key1):
        # speaker.say('performing Vigenère encryption using the given key')
        # speaker.runAndWait()
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        alpha = list(alpha)
        gamma = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        gamma = list(gamma)
        word = list(word)
        key = list(key1)
        # keeping record of index position of alphabets in key
        x = []
        for z in range(len(key)):
            if key[z] in alpha:
                x.append(alpha.index(key[z]))
            elif key[z] in gamma:
                x.append(gamma.index(key[z]))
        # keeping record of index position of spaces
        a = []
        for c in range(len(word)):
            if word[c] == ' ':
                a.append(c)
        # removing all spaces
        while word.count(' ') != 0:
            word.remove(' ')
        # encrypting using vigenere cipher
        for i in range(len(x)):
            for k in range(i, len(word), len(x)):
                if word[k] in alpha:
                    n = alpha.index(word[k])
                    num = n + x[i]
                    if n + x[i] > 25:
                        num2 = num - 25
                        beta = alpha[num2:] + alpha[:num2]
                        word[k] = beta[beta.index(word[k]) + x[i]]
                    else:
                        word[k] = alpha[alpha.index(word[k]) + x[i]]
                elif word[k] in gamma:
                    n = gamma.index(word[k])
                    if n + x[i] > 25:
                        num2 = (n + x[i]) - 25
                        beta = gamma[num2:] + gamma[:num2]
                        word[k] = beta[beta.index(word[k]) + x[i]]
                    else:
                        word[k] = gamma[n + x[i]]
        # adding spaces in original position
        new = []
        for j in range(len(word)):
            if j in a:
                new.insert(j, ' ')
            new.append(word[j])
        return ''.join(new)
        # speaker.say('encryption complete')
        # speaker.runAndWait()

    def rsa(self, word, p, q):
        def gcd(ele1, ele2):
            if ele2 == 0:
                return ele1
            else:
                return gcd(ele2, ele1 % ele2)

        text = ""
        N = p * q
        phiN = (p - 1) * (q - 1)
        e = 0
        for i in range(2, phiN):
            if gcd(N, i) == 1 and gcd(phiN, i) == 1:
                e = i
                break
        for j in word:
            if j.isupper():
                k = ord(j) - 64
                calc = (k ** e) % N
                text += str(calc) + ' '
            elif j.islower():
                k = ord(j) - 96
                calc = (k ** e) % N
                text += str(calc) + ' '
            else:
                text += j + ' '
        return text

    # def rsaAlgorithmE(self,word):
    #     text = ""
    #     N = self.p * self.q
    #     phiN = (self.p - 1) * (self.q - 1)
    #     for i in range(2, phiN):
    #         if gcd(N, i) == 1 and gcd(phiN, i) == 1:
    #             e = i
    #             break
    #     for j in self.t:
    #         if j.isupper():
    #             k = ord(j) - 64
    #             calc = (k ** e) % N
    #             text += str(calc) + ' '
    #         elif j.islower():
    #             k = ord(j) - 96
    #             calc = (k ** e) % N
    #             text += str(calc) + ' '
    #         else:
    #             text += j + ' '
    #     return text
    def new(self):
        k = ''
        cd = []
        new_pass = self.Pass
        # encrypting thrice
        for i in range(2):
            x = random.choice(['caesar', 'vig'])
            if x == 'caesar':
                K = x
                dir = random.choice(['l', 'r'])
                K = K + ' ' + dir
                n = random.randint(1, 26)
                K = K + ' ' + str(n)
                new_pass = self.caesar(new_pass, dir, n)
                k = k + K + ' '
            elif x == 'vig':
                K = x
                # creating key of random length (<=len(new_pass)) using random letters from new_pass
                key = []
                num = random.randint(1, len(new_pass))
                a = list(new_pass)
                while len(key) != num:
                    a1 = random.choice(a)
                    if a1 != ' ':
                        key.append(a1)
                key = ''.join(key)
                K = K + ' ' + key
                new_pass = self.vigenere(new_pass, key)
                k = k + K + ' '
        x = random.choice(self.types)
        if x == 'caesar':
            K = x
            dir = random.choice(['l', 'r'])
            K = K + ' ' + dir
            n = random.randint(1, 26)
            K = K + ' ' + str(n)
            new_pass = self.caesar(new_pass, dir, n)
            k = k + K + ' '
        elif x == 'vig':
            K = x
            # creating key of random length (<=len(new_pass)) using random letters from new_pass
            key = []
            num = random.randint(1, len(new_pass))
            a = list(new_pass)
            while len(key) != num:
                a1 = random.choice(a)
                if a1 != ' ':
                    key.append(a1)
            key = ''.join(key)
            K = K + ' ' + key
            new_pass = self.vigenere(new_pass, key)
            k = k + K + ' '
        # else:
        #     K = x
        #     prime = [i for i in range(len(new_pass) + 1)]
        #     p = 3
        #     prime[0] = False
        #     prime[1] = False
        #     while p * p <= len(new_pass) + 1:
        #         if prime[p] != False:
        #             for d in range(p * p, len(new_pass) + 1, p):
        #                 prime[d] = False
        #         p = p + 2
        #     a = []
        #     for j in range(len(prime)):
        #         if prime[j] != False:
        #             if prime[j] % 2 != 0 or prime[j] == 2:
        #                 a.append(prime[j])
        #     # choosing two random prime numbers
        #     x = random.choice(a)
        #     K = K + ' ' + str(x)
        #     a.remove(x)
        #     y = random.choice(a)
        #     K = K + ' ' + str(y)
        #     k = k + K + ' '
        #     new_pass = self.rsa(new_pass, x, y)
        cd.append(self.name)
        cd.append(new_pass)
        cd.append(k)
        # appending to a file
        file = open('file-1.txt', 'a')
        file.write(' '.join(cd))
        file.write('\n')
        file.close()


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

