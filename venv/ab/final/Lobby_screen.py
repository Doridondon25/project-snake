import threading
import tkinter
from tkinter import *
from register_screen import Register
import socket
from tkinter import ttk
from PIL import ImageTk, Image
from usersfinal import User
import tkinter.messagebox
import hashlib
import time
import tkinter as tk
from game_screen import *


class Lobby(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('800x800')
        self.title('Lobby page')
        self.waitinglist=["me"]


        self.img = Image.open(r'D:\pictuers\5319163.jpg')
        self.resize = self.img.resize((800, 800), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resize)
        self.imgLabel = Label(self, image=self.bg)
        self.imgLabel.pack(expand=NO)
        #self.welcome = Button(self, text='lobby', command=self.close)
        #self.welcome.place(x=400, y=400)

        self.lbl_headline = Label(self, text="Lobby :", font=("Arial", 100))
        self.lbl_headline.place(x=200, y=50)

        self.button = Button(self, text="Go back", command=self.close)
        self.button.place(x=750, y=0)

        #self.button = Button(self, text="A chat while waiting", command=self.send_message)
        #self.button.place(x=670, y=770)


        #self.click_btn = PhotoImage(file=r'C:\Users\User\PycharmProjects\pythonProject4\venv\ab\pic\settings.png')
        #self.img_label = Label(image=self.click_btn)
        #self.button1 = Button(self, image=self.click_btn, command=self.close, borderwidth=0, )
        #self.button1.place(x=0, y=0)
        #self.button1.size(x=100,y=100)
        self.lbl_countdown = Label(self, text="", font=("Hobo Std", 50))
        self.lbl_countdown.place(x=400, y=500)

        self.list = Listbox(self, height=3)
        username = self.parent.username
        self.list.insert(1, username)
        print(list)
        self.list.place(x=400, y=400)
        self.handle_waiting_for_player()

    def handle_waiting_for_player(self):
        self.Client_handler = threading.Thread(target=self.handle_waiting_for_players, args=())
        self.Client_handler.daemon = True
        self.Client_handler.start()

    def handle_waiting_for_players(self):
        #arr = ["lobby", player[1]]
        username = self.parent.username
        arr = ["lobby", username]
        data = ",".join(arr)
        self.parent.client_socket.send(data.encode())
        data = self.parent.client_socket.recv(1024).decode()
        arr = data.split(",")
        print(arr)
        if arr[1]== "wait":
            data = self.parent.client_socket.recv(1024).decode()
            data = data.split(",")
            print("player after waiting")
            self.list.insert(2, data[0])
            self.count_down()
            self.start_game()
            print("started")
        elif arr[1]== "start":
            print(arr[0] , " join us ")
            self.list.insert(2, arr[0])
            self.count_down()
            self.start_game()
            print("started")
            print("lets go")
            #try
    def start_game(self):
        self.window = SnakeGame(500, 500, 10, 10)
        self.window.grab_set()
        self.withdraw()



    def count_down(self):
        for i in range(5, 0, -1):
            self.lbl_countdown["text"] = str(i)
            self.update_idletasks()
            time.sleep(1)
        #self.lbl_countdown["text"] = "Starting Game!"

    def close(self):
        self.parent.deiconify()
        self.destroy()

