import threading
import tkinter
from tkinter import *
from register_screen import Register
import socket
from tkinter import ttk
from PIL import ImageTk, Image
from usersfinal import User
import  tkinter.messagebox
import hashlib
import time

class Login(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('1200x700')
        self.title('welcome page')
        self.configure(background='black')

        #self.img = Image.open(r'D:\pictuers\5319163.jpg')
        #self.resize = self.img.resize((800, 800), Image.Resampling.LANCZOS)
        #self.bg = ImageTk.PhotoImage(self.resize)
        #self.imgLabel = Label(self, image=self.bg)
        #self.imgLabel.pack(expand=NO)
        #self.welcome = Button(self, text='welcome', command=self.close)
        #self.welcome.place(x=400, y=400)

        self.click_btn = PhotoImage(file=r'C:\Users\User\PycharmProjects\pythonProject4\venv\ab\pic\snake1234.png')
        self.img_label = Label(image=self.click_btn)
        self.button = Button(self, image=self.click_btn, command=self.close, borderwidth=0,)
        self.button.place(x=0, y=0)




    def close(self):
        self.parent.deiconify()
        self.destroy()