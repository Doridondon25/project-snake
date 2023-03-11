import tkinter as tk
import tkinter


class GameOverScreen(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Game Over")
        self.geometry("500x400")
        self.configure(bg="black")

        self.sentence = "Game Over!"
        self.font_size = 40
        self.color = "white"

        self.label = tk.Label(self, text=self.sentence, font=("Book Antiqua", self.font_size), fg=self.color, bg="black")
        self.label.pack(expand=True)

        self.update_font_size()

    def update_font_size(self):
        if self.font_size == 40:
            self.font_size = 60
            self.color = "red"
        else:
            self.font_size = 40
            self.color = "white"

        self.label.config(font=("Book Antiqua", self.font_size), fg=self.color)

        self.after(1000, self.update_font_size)


#class Endgame(tkinter.Toplevel):
    #def __init__(self, parent):
        #super().__init__(parent)
        #self.parent = parent
        #self.geometry('800x800')
        #self.title('EndGame page')
        #self.waitinglist=["me"]


        #self.img = Image.open(r'D:\pictuers\5319163.jpg')
        #self.resize = self.img.resize((800, 800), Image.Resampling.LANCZOS)
        #self.bg = ImageTk.PhotoImage(self.resize)
        #self.imgLabel = Label(self, image=self.bg)
        #self.imgLabel.pack(expand=NO)
        #self.welcome = Button(self, text='lobby', command=self.close)
        #self.welcome.place(x=400, y=400)

        #self.lbl_headline = Label(self, text="Lobby :", font=("Arial", 100))
        #self.lbl_headline.place(x=200, y=50)

        #self.button = Button(self, text="Go back", command=self.close)
        #self.button.place(x=750, y=0)







#def play_music(filename):
    #playsound(filename)

#root = tkinter.Tk()
#root.title('sound player')  # giving the title for our window
#root.geometry("500x400")

# title on the screen you can modify it
#title = Label(root, text="music", bd=9, relief="groove",
              #font=("times new roman", 50, "bold"), bg="white", fg="green")
#title.pack(side="top", fill="x")

# list of music files
#music_files = [
    #('Soft Piano', 'D:\music\soft-piano-100-bpm-121529.mp3'),
    #('Epic Battle Music', 'D:\music\epic_battle_music_1-6275.mp3'),
    # add more music files here
#]

# making a button for each music file
#for name, file in music_files:
   # play_button = Button(root, text=name, font=("Helvetica", 20),
                         #relief="groove", command=lambda file=file: play_music(file))
    #play_button.pack(pady=20)

#info = Label(root, text="Select a song from the list above to play it ",
             #font=("times new roman", 10, "bold")).pack(pady=20)

#root.mainloop()

#lobby.mainloop()