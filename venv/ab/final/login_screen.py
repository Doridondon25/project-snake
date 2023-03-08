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

        self.click_btn = PhotoImage(file=r'C:\Users\User\PycharmProjects\pythonProject4\venv\ab\pic\snake1234.png')
        self.img_label = Label(image=self.click_btn)
        self.button = Button(self, image=self.click_btn, command=self.close, borderwidth=0,)
        self.button.place(x=0, y=0)




    def close(self):
        self.parent.deiconify()
        self.destroy()