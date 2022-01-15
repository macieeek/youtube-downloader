import requests
import tkinter as tk
from tkinter import messagebox
from pages.page import Page
from pytube import YouTube
from helper import Helper


class MainPanelPage(Page):
    def __init__(self):
        Page.__init__(self)
        self.helper = Helper()

        self.show_content()

    def show_content(self):
        title_label = tk.Label(self, text="Podaj link do wideo na YouTube", font=("Arial", 20))
        title_label.place(x=60, y=30)

        self.url_video_input = tk.Entry(self, font=12)
        self.url_video_input.place(width=390, height=30, x=60, y=80)

        self.confirm_button = tk.Button(self, text="Pobierz", font=11, borderwidth=4, relief="groove", command=self.download_video)
        self.confirm_button.place(y=130, x=196, width=125, height=35)

        self.download_status_label = tk.Label(self, text="Trwa pobieranie, może to chwilę potrwać...", fg="green", font=("Arial", 14))


    def download_video(self):
        try:
            video = YouTube(self.url_video_input.get())

            self.download_status_label.place(y=180, x=78)
            self.confirm_button["state"] = "disabled"
            self.update()

            video.streams.get_highest_resolution().download(self.helper.get_download_path())

            self.confirm_button["state"] = "normal"
            self.download_status_label.place_forget()
            self.update()

            message_box = tk.messagebox.showinfo(title="Pomyślnie pobrano!", message="Wideo zostało pobrane pomyślnie!")
        except:
            message_box = tk.messagebox.showinfo(title="Wystąpił błąd", message="Coś poszło nie tak... Sprawdź poprawność linka.")

        self.download_status_label.place_forget()