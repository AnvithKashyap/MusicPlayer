import os
import webbrowser
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tkinter import Tk, Label, Entry, Button

class MusicSearchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Search App")
        self.master.geometry("400x150")

        self.youtube_api_service_name = "youtube"
        self.youtube_api_version = "v3"
        self.api_key = "AIzaSyC0jXSfS4RhKHp2TiuJinbh2XKDDDrnvdw"  # Replace with your actual YouTube API key

        self.create_widgets()

    def create_widgets(self):
        # Entry Widget for Search
        self.search_entry = Entry(self.master, width=30)
        self.search_entry.pack(pady=10)

        # Search Button
        self.search_button = Button(self.master, text="Search", command=self.search_music)
        self.search_button.pack(pady=5)

        # Open in Browser Button
        self.open_button = Button(self.master, text="Open in Browser", command=self.open_in_browser)
        self.open_button.pack(pady=5)

        # Label to display the video title
        self.title_label = Label(self.master, text="")
        self.title_label.pack(pady=5)

    def search_music(self):
        query = self.search_entry.get()
        if query:
            youtube = build(self.youtube_api_service_name, self.youtube_api_version, developerKey=self.api_key)
            request = youtube.search().list(q=query, part="snippet", type="video", maxResults=1)
            response = request.execute()

            if 'items' in response:
                video_title = response['items'][0]['snippet']['title']
                video_id = response['items'][0]['id']['videoId']
                self.video_url = f"https://www.youtube.com/watch?v={video_id}"
                print(f"Found video: {self.video_url}")

                # Update the label with the video title
                self.title_label.config(text=f"Found video: {video_title}")
            else:
                print("No videos found.")
                self.video_url = None
                self.title_label.config(text="No videos found.")

    def open_in_browser(self):
        if hasattr(self, 'video_url') and self.video_url:
            webbrowser.open(self.video_url)
        else:
            print("Please search for a video first.")

if __name__ == "__main__":
    root = Tk()
    music_search_app = MusicSearchApp(root)
    root.mainloop()
