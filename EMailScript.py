# English
# Most of this was written by me (https://github.com/HUSDI)
# The "algorithm" created to switch between windows isn't mine!
# I'd link his github if i'd find him.
# German
# Das meiste meines Codes wurde von mir geschrieben.
# Der Code zum "hoch- und herbsenken" der frames wurde von einem anderen gemacht.
# Ich würde sein github verlinken, finde ihn jedoch nicht mehr.
import tkinter as tk
from tkinter import ttk
import ctypes
import webbrowser
import json


LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Arial", 10)
SMALL_FONT = ("Arial", 8)


def popupmessage(msg):
    popup = tk.Tk()
    popup.iconbitmap('data/madeThisIn10Secs.ico')
    popup.geometry("{}x{}".format(int(user32.GetSystemMetrics(0)/5), int(user32.GetSystemMetrics(1)/6)))

    popup.wm_title("Warning!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)
    B1 = ttk.Button(popup, text='Okay', command=popup.destroy)
    B1.pack(side='bottom')
    popup.mainloop()


def opentab(url):
    webbrowser.open(url)


class EMailPrg(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.wm_title("TKinter Template created by HUSDI (E.S.)")

        container = ttk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        startmenu = tk.Menu(menubar, tearoff=False)
        startmenu.add_command(label='Website', command=lambda: opentab("https://github.com/HUSDI"))
        startmenu.add_command(label='Test Popup', command=lambda: popupmessage('This is a test popup'))
        startmenu.add_separator()
        startmenu.add_command(label='Close', command=quit)
        menubar.add_cascade(label='Start', menu=startmenu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (LoginPage, RegisterPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')
        
        self.show_frame(LoginPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def checkLogin(self, username, password):

        with open('data/yourlogininfo.json') as f:
            content = json.load(f)

        try:
            if content[username] == password:
                self.show_frame(PageOne)
            else:
                popupmessage('Username or password is wrong!')
        except:
            popupmessage('Username or password is wrong!')


    def register(self, username, FirstPW, SecPW):

        with open('data/yourlogininfo.json') as f:
            content = json.load(f)

        if username in content:
            popupmessage('Username is already taken!')
        elif len(username) < 5:
            popupmessage('Username must contain\nat least 5 characters!')
        elif len(FirstPW) < 8:
            popupmessage('Password must contain\nat least 8 characters!')
        elif FirstPW != SecPW:
            popupmessage('Passwords are not equal!')
        else:
            content[username] = FirstPW

            with open('data/yourlogininfo.json', 'w') as f:
                conv = json.dumps(content)
                f.write(conv)
                self.show_frame(LoginPage)


class LoginPage(ttk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        loginLabel = ttk.Label(self, text='Login', font=LARGE_FONT)
        loginLabel.grid(row=0, column=0, sticky='w')

        placholder1 = ttk.Label(self, text='').grid(row=1, column=0)

        usernLabel = ttk.Label(self, text='Username:', font=NORM_FONT)
        usernLabel.grid(row=2, column=0, sticky='e')

        usernameEnt = ttk.Entry(self)
        usernameEnt.grid(row=2, column=1)

        passLabel = ttk.Label(self, text='Password:', font=NORM_FONT)
        passLabel.grid(row=3, column=0, sticky='e')

        passwordEntry = ttk.Entry(self)
        passwordEntry.grid(row=3, column=1)

        placholder2 = ttk.Label(self, text='').grid(row=4, column=0)

        button1 = ttk.Button(self, text='Login',
                            command=lambda: controller.checkLogin(usernameEnt.get().lower(), passwordEntry.get()))
        button1.grid(row=5, column=0, sticky='w')

        button2 = ttk.Button(self, text='Register',
                            command=lambda: controller.show_frame(RegisterPage))
        button2.grid(row=5, column=1, sticky='e')


class RegisterPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        loginLabel = ttk.Label(self, text='Register', font=LARGE_FONT)
        loginLabel.grid(row=0, column=0, sticky='w')

        placeholder1 = ttk.Label(self, text='').grid(row=1, column=0)

        usernLabel = ttk.Label(self, text='Username:', font=NORM_FONT)
        usernLabel.grid(row=2, column=0, sticky='e')

        usernameEnt = ttk.Entry(self)
        usernameEnt.grid(row=2, column=1)

        passLabel = ttk.Label(self, text='Password:', font=NORM_FONT)
        passLabel.grid(row=3, column=0, sticky='e')

        passwordEntry = ttk.Entry(self)
        passwordEntry.grid(row=3, column=1)

        confPasswordLabel = ttk.Label(self, text='Confirm Password:', font=NORM_FONT)
        confPasswordLabel.grid(row=4, column=0, sticky='e')

        confPasswordEntry = ttk.Entry(self)
        confPasswordEntry.grid(row=4, column=1)

        placeholder2 = ttk.Label(self, text='').grid(row=5, column=0)

        button1 = ttk.Button(self, text='Register',
                            command=lambda: controller.register(usernameEnt.get().lower(),
                                                                passwordEntry.get(), confPasswordEntry.get()))
        button1.grid(row=6, column=1, sticky='e')

        button1 = ttk.Button(self, text='Go Back',
                            command=lambda: controller.show_frame(LoginPage))
        button1.grid(row=6, column=0, sticky='w')


class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text='Page One', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Login',
                            command=lambda: controller.show_frame(LoginPage))
        button1.pack()

        button2 = ttk.Button(self, text='Exit',
                            command=quit)
        button2.pack()


user32 = ctypes.windll.user32
app = EMailPrg()
app.iconbitmap("data/madeThisIn10Secs.ico")
# Gets screen size, devides it by 2 and sets window size to the results
app.geometry("{}x{}".format(int(user32.GetSystemMetrics(0)/2), int(user32.GetSystemMetrics(1)/2)))
app.mainloop()

