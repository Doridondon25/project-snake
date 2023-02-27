import threading
import tkinter
from tkinter import *
from register_screen import Register
import socket
from tkinter import ttk
from login_screen import Login
from PIL import ImageTk, Image
from usersfinal import User
import  tkinter.messagebox
import hashlib
import time
from Lobby_screen import Lobby
from music_player import MusicPlayer
from tkinter import colorchooser
import tkinter as tk


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Main Window')
        self.userdb = User()
        self.username= ""

        #self.start = ""
        #self.img = Image.open(r'C:\Users\User\PycharmProjects\pythonProject4\venv\ab\pic\zenitzu.png')
        #self.img = Image.open(r'D:\pictuers\5319163.jpg')
        #self.resize = self.img.resize((800, 800), Image.Resampling.LANCZOS)
        #self.bg = ImageTk.PhotoImage(self.resize)
        #self.imgLabel = Label(self, image=self.bg)
        #self.imgLabel.pack(expand=YES)

        self.lbl_email = Label(self, width=20,height=2, text="email :")#fg="white")#bg="black")
        self.lbl_email.place(x=225, y=50)
        self.email = Entry(self, width=20)
        self.email.place(x=200, y=80)

        self.lbl_password = Label(self, width=10, text="password :")
        self.lbl_password.place(x=225, y=100)
        self.password = Entry(self, width=20, show="*")
        self.password.place(x=200, y=130)

        self.btn_hide = Button(self, text="Music", command=self.hide)
        self.btn_hide.place(x=460 ,y=10)

        self.btn_color = Button(self, text="color", command=self.backgroundcolor)
        self.btn_color.place(x=460, y=40)

        self.btn_login = Button(self, text="0", command=self.open_login())
        #self.btn_login.place(x=200, y=200)
        self.btn_login2 = Button(self, text="Login please", command= self.login_1,fg="black",bg="green")
        self.btn_login2.place(x=200, y=200)

        #self.btn_login1 = Button(self, text=" Return to home", command=self.open_login)#usersfinal.login_1
        #self.btn_login1.place(x=200, y=400)

        self.click_btn = PhotoImage(file=r'C:\Users\User\PycharmProjects\pythonProject4\venv\ab\pic\return (1).png')
        self.img_label = Label(image=self.click_btn)
        self.button = Button(self, image=self.click_btn, command=self.open_login, borderwidth=0, )
        self.button.place(x=10, y=460)

        self.btn_register = Button(self, text='Go to Register page', command=self.open_register)
        self.btn_register.place(x=400, y=400)
        self.handle_thread_socket()

        self.data = StringVar()
        self.datalabel = Label(self, textvariable=self.data,background= "yellow", width = (20))
        self.datalabel.place(x=400, y=100)



    def open_register(self):
        window = Register(self)
        window.grab_set()
        self.withdraw()

    def login_1(self):
        email = self.email.get()
        print(email)
        password = self.password.get()
        print(password)
        #arr = User().return_user_by_email_password(email, password)
        arr = ["login", email, password]
        insert = ",".join(arr)
        print(insert)
        self.client_socket.send(insert.encode())
        self.username = self.client_socket.recv(1024).decode()
        data = self.client_socket.recv(1024).decode()
        print("-----")
        print(data)
        try:
            if not arr:
                self.data.set("Error")
                #messagebox.showerror("error massage", 'error')
                return False
            else:
                self.data.set(data)
                self.open_lobby()
                return True

        except:
            #messagebox.showerror("error massage", 'error')
            return False

    def open_login(self):
        window = Login(self)
        window.grab_set()
        self.withdraw()


    def open_lobby(self):
        window = Lobby(self)
        window.grab_set()
        self.withdraw()

    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 1804))
        data = self.client_socket.recv(1024).decode()
        print("data"+data)
        print("hi", self.client_socket)

    def hide(self):
        player = MusicPlayer()
        player.run()
        #pass
        print("hide")

    def backgroundcolor(self):
        c_code = colorchooser.askcolor()
        self.configure(bg=c_code[1])
        print(c_code)






if __name__ == "__main__":
    app = App()
    app.mainloop()