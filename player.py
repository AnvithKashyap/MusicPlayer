import os
import pygame
from tkinter import Tk, Label, Button, filedialog

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("500x250")

        self.track = None
        self.paused = False
        self.paused_at = 0  # To store the position where the music was paused

        self.create_widgets()

    def create_widgets(self):
        # Track Label
        self.track_label = Label(self.master, text="No Track Playing", font=("Helvetica", 12))
        self.track_label.pack(pady=10)

        # Buttons
        self.select_button = Button(self.master, text="Select Track", command=self.load_track)
        self.select_button.pack(pady=5)

        self.play_button = Button(self.master, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)

        self.pause_button = Button(self.master, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=5)

        self.stop_button = Button(self.master, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.resize_button = Button(self.master, text="Enlarge Window", command=self.enlarge_window)
        self.resize_button.pack(pady=5)

    def load_track(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("Music Files", "*.mp3")])
        if file_path:
            self.track = file_path
            self.track_label.config(text=os.path.basename(file_path))

    def play_music(self):
        if self.track:
            pygame.mixer.init(frequency=44100)  # Explicitly set the sample rate to 44.1 kHz
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.load(self.track)
                pygame.mixer.music.play(start=self.paused_at)
                self.paused_at = 0  # Reset the paused position

    def pause_music(self):
        if pygame.mixer.music.get_busy() and not self.paused:
            pygame.mixer.music.pause()
            self.paused_at = pygame.mixer.music.get_pos()  # Store the current position
            self.paused = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.paused_at = 0
        self.paused = False

    def enlarge_window(self):
        current_width = self.master.winfo_width()
        current_height = self.master.winfo_height()
        new_width = current_width + 100
        new_height = current_height + 50
        self.master.geometry(f"{new_width}x{new_height}")

if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
