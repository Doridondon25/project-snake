import pygame
import tkinter as tk
from tkinter import ttk

class MusicPlayer:
    def __init__(self):
        # Define a list of song names and paths
        self.songs = [
            {"name": "Piano", "path": 'D:\music\soft-piano-100-bpm-121529.mp3'},
            {"name": "Battle", "path": 'D:\music\epic_battle_music_1-6275.mp3'},
            {"name": "Dark", "path": 'D:\music\dark-background-sounds-52324.mp3'},
            {"name": "ANNOYING", "path": 'D:\music\cottagecore-17463.mp3'},
            {"name": "Tata", "path": r'D:\music\taratata-6264.mp3'},
            {"name": "Letsgo", "path": 'D:\music\gamemusic-6082.mp3'},
            {"name": "cyber-town", "path": 'D:\music\cyber-town-simcity-style-music-22907.mp3'},
            {"name": "rar", "path": r'D:\music\1-soundtrack-18034.mp3'},
            {"name": "spookyy", "path": r'D:\music\spooky-halloween-effects-with-thunder-121665.mp3'},
            {"name": "stop music", "path": 'D:\music\infinitely-loud-silence-ils-74283.mp3'},
            # Add more songs here
        ]

        # Initialize Pygame
        pygame.init()

        # Create the GUI window
        self.root = tk.Tk()
        self.root.title("Music Player")

        # Create the listbox to display the songs
        self.listbox = tk.Listbox(self.root,fg="green",bg="black",selectbackground="gray",selectforeground="black")
        self.listbox.pack()

        # Populate the listbox with the song names
        for song in self.songs:
            self.listbox.insert("end", song["name"])


        # Create a play button
        self.play_button = tk.Button(self.root, text="Play", command=self.play_song)
        self.play_button.pack()

    # Function to play the selected song
    def play_song(self):
        selected_song = self.listbox.get(self.listbox.curselection())
        for song in self.songs:
            if song["name"] == selected_song:
                pygame.mixer.music.load(song["path"])
                pygame.mixer.music.play()

    # Start the GUI event loop
    def run(self):
        self.root.mainloop()
