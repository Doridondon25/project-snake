import tkinter as tk
import pygame

def play_music(music_file):
    pygame.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

root = tk.Tk()
root.title("Music Player")

playlist = ["D:\music\spooky-halloween-effects-with-thunder-121665.mp3", "song2.mp3", "song3.mp3"]

for music_file in playlist:
    tk.Button(root, text=music_file, command=lambda file=music_file: play_music(file)).pack()

root.mainloop()