import json
import tkinter as tk
from tkinter import messagebox
from pages.page import Page
from pytube import YouTube
from helper import Helper


class MainPanelPage(Page):
    def __init__(self, settings):
        Page.__init__(self)
        self.helper = Helper()
        self.settings = settings

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
        if len(self.url_video_input.get()) < 3:
            return

        if not self.helper.check_internet_connection():
            tk.messagebox.showerror(title="Brak połączenia z internetem", message="Sprawdź swoje połączenie z internetem.")
            return
        try:
            video = YouTube(self.url_video_input.get())

            self.download_status_label.place(y=180, x=78)
            self.confirm_button["state"] = "disabled"
            self.update()

            video = self.handle_settings(video)

            if self.settings.directory == "dekstop": directory = self.helper.get_desktop_path()
            elif self.settings.directory == "downloads": directory = self.helper.get_download_path()
            elif self.settings.directory == "custom": directory = self.settings.custom_path_directory
            else: directory = self.helper.get_desktop_path()
            video.download(directory)

            self.confirm_button["state"] = "normal"
            self.download_status_label.place_forget()
            self.update()

            tk.messagebox.showinfo(title="Pomyślnie pobrano!", message="Wideo zostało pobrane pomyślnie!")
        except:
            tk.messagebox.showerror(title="Wystąpił błąd", message="Coś poszło nie tak... Sprawdź poprawność linka.")

    def handle_settings(self, video):
        video = video.streams

        # selected type is audio
        if self.settings.type == "audio":
            return video.filter(
                file_extension=self.settings.extension,
                type="audio"
            ).first()

        # selected type is video
        if self.settings.resolution == "lowest":
            video = video.filter(file_extension=self.settings.extension).order_by("resolution").asc().first()
        elif self.settings.resolution == "highest":
            video = video.filter(file_extension=self.settings.extension).order_by("resolution").desc().first()
        else:
            # check if selected video resolution is higher than available in video
            test_resolution_video = video.filter(file_extension=self.settings.extension).order_by("resolution").desc().first()
            if test_resolution_video.resolution < self.settings.resolution:
                return test_resolution_video

            video = video.filter(
                res=self.settings.resolution,
                file_extension=self.settings.extension
            ).first()

        return video
