import tkinter as tk
from tkinter import ttk
from pages.page import Page
from helper import Helper

radio_type_variable = ""
radio_resolution_variable = ""


class SettingsPage(Page):
    def __init__(self, settings):
        Page.__init__(self)
        self.helper = Helper()
        self.settings = settings

        self.show_content()

    def show_content(self):
        self.show_type_options()
        self.show_resolution_options()

        #
        # extension_label = tk.Label(self, text="Rozszerzenie pliku", font=("Arial", 15))
        # extension_label.place(x=50, y=90)
        #
        # directory_label = tk.Label(self, text="Katalog pobrania", font=("Arial", 15))
        # directory_label.place(x=50, y=120)
        #
        # custom_directory_label = tk.Label(self, text="Własny katalog pobrania", font=("Arial", 15))
        # custom_directory_label.place(x=50, y=150)

    def show_type_options(self):
        labelframe_type_widget = tk.LabelFrame(self, text="Rodzaj pobieranego pliku", font=("Arial", 14), width=385, height=60)
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


    def change_type_option(self, value):
        if value == "audio": self.settings.type = "audio"
        elif value == "video": self.settings.type = "video"

    def change_resolution_option(self, value):
        if value == "lowest": self.settings.resolution = "lowest"
        elif value == "360p": self.settings.resolution = "360p"
        elif value == "720p": self.settings.resolution = "720p"
        elif value == "highest": self.settings.resolution = "highest"
