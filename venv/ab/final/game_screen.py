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
import tkinter as tk
import tkinter
import random
import math


class SnakeGame:
    def __init__(self, width, height, snake_block, apple_block):
        self.width = width
        self.height = height
        self.snake_block = snake_block
        self.apple_block = apple_block
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        self.score = tk.StringVar()
        self.score.set("Score: 0")
        self.score_label = tk.Label(self.root, textvariable=self.score, font=("Arial", 14))
        self.score_label.pack()
        self.snake_head = [200, 200]
        self.snake_list = [[200, 200], [190, 200], [180, 200]]
        self.direction = "UP"
        self.pointssnake1 = 0
        # self.snake_color = "blue"
        self.create_snake(self.snake_list)
        self.create_apple()
        self.canvas.bind_all("<KeyPress-Up>", self.move_up)
        self.canvas.bind_all("<KeyPress-Down>", self.move_down)
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def move_up(self, event):
        print("up")
        self.direction = "UP"
        self.snake_head[1] -= self.snake_block
        self.snake_list.insert(0, list(self.snake_head))
        self.snake_list.pop()
        self.canvas.delete("snake")
        self.create_snake(self.snake_list)
        self.check_collision()
        self.exit()

    def move_down(self, event):
        print("DOWN")
        self.direction = "DOWN"
        self.snake_head[1] += self.snake_block
        self.snake_list.insert(0, list(self.snake_head))
        self.snake_list.pop()
        self.canvas.delete("snake")
        self.create_snake(self.snake_list)
        self.check_collision()
        self.exit()

    def move_left(self, event):
        print("LEFT")
        self.direction = "LEFT"
        self.snake_head[0] -= self.snake_block
        self.snake_list.insert(0, list(self.snake_head))
        self.snake_list.pop()
        self.canvas.delete("snake")
        self.create_snake(self.snake_list)
        self.check_collision()
        self.exit()

    def move_right(self, event):
        print("RIGHT")
        self.direction = "RIGHT"
        self.snake_head[0] += self.snake_block
        self.snake_list.insert(0, list(self.snake_head))
        self.snake_list.pop()
        self.canvas.delete("snake")
        self.create_snake(self.snake_list)
        self.check_collision()
        self.exit()

    def exit(self):
        if self.snake_head[0] >= self.width or self.snake_head[0] < 0 or self.snake_head[1] >= self.height or \
                self.snake_head[1] < 0:
            self.root.destroy()
            self.root.quit()
            print("End of game")
            print("your score is " + str(self.pointssnake1))
        for block in self.snake_list[1:]:
            if self.snake_head[0] == block[0] and self.snake_head[1] == block[1]:
                self.root.destroy()
                self.root.quit()
                print("End of game")
                print("your score is " + str(self.pointssnake1))

    def start(self):
        print("start")
        self.root.mainloop()

    def random_x(self):
        return random.randint(0, self.width - self.apple_block)

    def random_y(self):
        return random.randint(0, self.height - self.apple_block)

    def create_snake(self, snake_list):
        self.snake_list = snake_list
        for x, y in self.snake_list:
            self.canvas.create_rectangle(x, y, x + self.snake_block, y + self.snake_block, fill="black",
                                         tag="snake")

    def create_apple(self):
        self.apple_x = self.random_x()
        self.apple_y = self.random_y()
        self.canvas.create_oval(self.apple_x, self.apple_y, self.apple_x + self.apple_block,
                                self.apple_y + self.apple_block, fill="red", tag="apple")

    def check_collision(self):
        apple_center_x = self.apple_x + self.apple_block / 2
        apple_center_y = self.apple_y + self.apple_block / 2
        snake_center_x = self.snake_head[0] + self.snake_block / 2
        snake_center_y = self.snake_head[1] + self.snake_block / 2
        distance = math.sqrt((apple_center_x - snake_center_x) ** 2 + (apple_center_y - snake_center_y) ** 2)
        if distance < (self.snake_block + self.apple_block) / 2:
            self.pointssnake1 += 1
            print("you ate an apple")
            print("you got a point")
            self.score.set(f"Score: {self.pointssnake1}")
            self.score_label.config(text=f"Score: {self.pointssnake1}")
            self.canvas.delete("apple")
            self.create_apple()
            self.snake_list.append([0, 0])


#game = SnakeGame(500, 500, 10, 10)
#game.start()







