import tkinter as tk
from tkinter import ttk
from playsound import playsound

# Define a list of song names and paths
songs = [
    {"name": "Soft Piano", "path": 'D:\music\soft-piano-100-bpm-121529.mp3'},
    {"name": "Epic Battle Music", "path": 'D:\music\epic_battle_music_1-6275.mp3'},
    {"name": "Song 3", "path": "path/to/song3.mp3"},
    # Add more songs here
]

# Create the GUI window
root = tk.Tk()
root.title("Music Player")

# Create the listbox to display the songs
listbox = tk.Listbox(root)
listbox.pack()

# Populate the listbox with the song names
for song in songs:
    listbox.insert("end", song["name"])

# Function to play the selected song
def play_song():
    selected_song = listbox.get(listbox.curselection())
    for song in songs:
        if song["name"] == selected_song:
            playsound(song["path"])

# Create a play button
play_button = tk.Button(root, text="Play", command=play_song)
play_button.pack()

# Start the GUI event loop
root.mainloop()
