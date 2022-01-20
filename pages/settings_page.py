import tkinter as tk
from tkinter import ttk
from pages.page import Page
from helper import Helper

# set variables there because of tkinter radio buttons bug
radio_type_variable = ""
radio_resolution_variable = ""
radio_extension_variable = ""
radio_directory_variable = ""


class SettingsPage(Page):
    def __init__(self, settings):
        Page.__init__(self)
        self.helper = Helper()
        self.settings = settings

        self.show_content()

    def show_content(self):
        self.show_type_options()
        self.show_resolution_options()
        self.show_extension_options()
        self.show_directory_options()

        #
        # custom_directory_label = tk.Label(self, text="Własny katalog pobrania", font=("Arial", 15))
        # custom_directory_label.place(x=50, y=150)

    def show_type_options(self):
        labelframe_type_widget = tk.LabelFrame(self, text="Rodzaj", font=("Arial", 14), width=385, height=60)
        labelframe_type_widget.place(x=30, y=10)

        global radio_type_variable
        radio_type_variable = tk.StringVar()
        radio_type_variable.set(self.settings.type)
        radio_button_video = tk.Radiobutton(labelframe_type_widget, variable=radio_type_variable, value="video", text="Dźwięk oraz wideo", font=("Arial", 12),
                                            command=lambda: self.change_type_option("video"))
        radio_button_video.place(x=20, y=1)

        radio_button_audio = tk.Radiobutton(labelframe_type_widget, variable=radio_type_variable, value="audio", text="Tylko dźwięk", font=("Arial", 12),
                                            command=lambda: self.change_type_option("audio"))
        radio_button_audio.place(x=240, y=1)
        
    def show_resolution_options(self):
        labelframe_resolution_widget = tk.LabelFrame(self, text="Rozdzielczość", font=("Arial", 14), width=455, height=60)
        labelframe_resolution_widget.place(x=30, y=80)

        global radio_resolution_variable
        radio_resolution_variable = tk.StringVar()
        radio_resolution_variable.set(self.settings.resolution)

        radio_button_lowest_resolution = tk.Radiobutton(labelframe_resolution_widget, variable=radio_resolution_variable, value="lowest", text="Najniższa",
                                                        font=("Arial", 13), command=lambda: self.change_resolution_option("lowest"))
        radio_button_lowest_resolution.place(x=20, y=1)

        radio_button_360p_resolution = tk.Radiobutton(labelframe_resolution_widget, variable=radio_resolution_variable, value="360p", text="360p",
                                                        font=("Arial", 13), command=lambda: self.change_resolution_option("360p"))
        radio_button_360p_resolution.place(x=140, y=1)

        radio_button_720p_resolution = tk.Radiobutton(labelframe_resolution_widget, variable=radio_resolution_variable, value="720p", text="720p",
                                                      font=("Arial", 13), command=lambda: self.change_resolution_option("720p"))
        radio_button_720p_resolution.place(x=230, y=1)

        radio_button_highest_resolution = tk.Radiobutton(labelframe_resolution_widget, variable=radio_resolution_variable, value="highest", text="Najwyższa",
                                                        font=("Arial", 13), command=lambda: self.change_resolution_option("highest"))
        radio_button_highest_resolution.place(x=320, y=1)

    def show_extension_options(self):
        labelframe_extension_widget = tk.LabelFrame(self, text="Rozszerzenie", font=("Arial", 14), width=230, height=60)
        labelframe_extension_widget.place(x=30, y=150)

        global radio_extension_variable
        radio_extension_variable = tk.StringVar()
        radio_extension_variable.set(self.settings.extension)
        radio_button_mp4 = tk.Radiobutton(labelframe_extension_widget, variable=radio_extension_variable, value="mp4", text="MP4", font=("Arial", 12),
                                            command=lambda: self.change_extension_option("mp4"))
        radio_button_mp4.place(x=20, y=1)

        radio_button_webm = tk.Radiobutton(labelframe_extension_widget, variable=radio_extension_variable, value="webm", text="WEBM", font=("Arial", 12),
                                            command=lambda: self.change_extension_option("webm"))
        radio_button_webm.place(x=120, y=1)

    def show_directory_options(self):
        labelframe_directory_widget = tk.LabelFrame(self, text="Rozszerzenie", font=("Arial", 14), width=380, height=60)
        labelframe_directory_widget.place(x=30, y=220)

        global radio_directory_variable
        radio_directory_variable = tk.StringVar()
        radio_directory_variable.set(self.settings.directory)

        radio_button_desktop = tk.Radiobutton(labelframe_directory_widget, variable=radio_directory_variable, value="desktop",
                                           text="Pulpit", font=("Arial", 12),
                                           command=lambda: self.change_directory_option("desktop"))
        radio_button_desktop.place(x=20, y=1)

        radio_button_downloads = tk.Radiobutton(labelframe_directory_widget, variable=radio_directory_variable, value="downloads",
                                          text="Pobrane", font=("Arial", 12),
                                          command=lambda: self.change_directory_option("downloads"))
        radio_button_downloads.place(x=114, y=1)

        radio_button_custom = tk.Radiobutton(labelframe_directory_widget, variable=radio_directory_variable,
                                                value="custom",
                                                text="Własny folder", font=("Arial", 12),
                                                command=lambda: self.change_directory_option("custom"))
        radio_button_custom.place(x=229, y=1)


    def change_type_option(self, value):
        if value == "audio": self.settings.type = "audio"
        elif value == "video": self.settings.type = "video"

    def change_resolution_option(self, value):
        if value == "lowest": self.settings.resolution = "lowest"
        elif value == "360p": self.settings.resolution = "360p"
        elif value == "720p": self.settings.resolution = "720p"
        elif value == "highest": self.settings.resolution = "highest"

    def change_extension_option(self, value):
        if value == "mp4": self.settings.extension = "mp4"
        elif value == "webm": self.settings.extension = "webm"

    def change_directory_option(self, value):
        if value == "downloads": self.settings.directory = "downloads"
        elif value == "desktop": self.settings.directory = "desktop"
        elif value == "custom": self.settings.directory = "custom"