import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from usersfinal import  *
import threading
import tkinter
from tkinter import *
import socket
from tkinter import ttk
from PIL import ImageTk, Image
from usersfinal import User
import  tkinter.messagebox
import hashlib

class Register(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('500x500')
        self.title('Register page')
        self.userdb= User()
        self.img = Image.open(r'D:\pictuers\5319163.jpg')
        self.resize = self.img.resize((500, 500), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resize)
        self.imgLabel = Label(self, image=self.bg)
        self.imgLabel.pack(expand=YES)

        self.create_gui()



    def create_gui(self):

        self.lbl_email = Label(self, width=10, text="email :")
        self.lbl_email.place(x=10, y=50)
        self.email = Entry(self, width=20)
        self.email.place(x=100, y=50)

        self.lbl_password = Label(self, width=10, text="password :")
        self.lbl_password.place(x=10, y=100)
        self.password = Entry(self, width=20)
        self.password.place(x=100, y=100)

        self.lbl_firstname = Label(self, width=10, text="firstname :")
        self.lbl_firstname.place(x=10, y=150)
        self.firstname = Entry(self, width=20)
        self.firstname.place(x=100, y=150)

        self.buttonPlus = Button(self, text="register", command=self.handle_add_user, width=20, background="green")
        self.buttonPlus.place(x=10, y=200)

        self.click_btn = PhotoImage(file=r'C:\Users\User\PycharmProjects\pythonProject4\venv\ab\pic\return (1).png')
        self.img_label = Label(image=self.click_btn)
        self.button = Button(self, image=self.click_btn, command=self.close, borderwidth=0, )
        self.button.place(x=10, y=460)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.register_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def register_user(self):
        try:
            print("register")
            arr = ["register", self.email.get(), self.password.get(), self.firstname.get()]
            str_insert = ",".join(arr)
            print(str_insert)
            self.parent.client_socket.send(str_insert.encode())
            data = self.parent.client_socket.recv(1024).decode()
            print(data)
            if data[0]== "s":
                messagebox.showinfo("SUCCESS", "Registered")
            elif data[0] == "f":
                messagebox.showerror("ERROR", "Failed Register")
        except:
            messagebox.showerror("ERROR", "Failed Register")


    def close(self):
        self.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen