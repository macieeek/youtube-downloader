import tkinter as tk
from tkinter import ttk
from pages.page import Page
from helper import Helper

radio_button_variable = ""


class SettingsPage(Page):
    def __init__(self, settings):
        Page.__init__(self)
        self.helper = Helper()
        self.settings = settings

        self.show_content()

    def show_content(self):
        self.show_type_options()
        self.show_resolution_options()

        # resolution_label = tk.Label(self, text="Rozdzielczość", font=("Arial", 15))
        # resolution_label.place(x=50, y=30)
        #
        # type_label = tk.Label(self, text="Rodzaj", font=("Arial", 15))
        # type_label.place(x=50, y=60)
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
        labelframe_options_widget = tk.LabelFrame(self, text="Rodzaj pobieranego pliku", font=("Arial", 15), width=453, height=70)
        labelframe_options_widget.place(x=30, y=25)

        global radio_button_variable
        radio_button_variable = tk.StringVar()
        radio_button_variable.set(self.settings.type)
        radio_button_video = tk.Radiobutton(labelframe_options_widget, variable=radio_button_variable, value="video", text="Dźwięk oraz wideo", font=("Arial", 13),
                                            command=lambda: self.change_type_option("video"))
        radio_button_video.place(x=30, y=7)

        radio_button_audio = tk.Radiobutton(labelframe_options_widget, variable=radio_button_variable, value="audio", text="Tylko dźwięk", font=("Arial", 13),
                                            command=lambda: self.change_type_option("audio"))
        radio_button_audio.place(x=300, y=7)


    def show_resolution_options(self):
        labelframe_resolution_widget = tk.LabelFrame(self, text="Rozdzielczość", font=("Arial", 15), width=453, height=100)
        labelframe_resolution_widget.place(x=30, y=210)

    def change_type_option(self, value):
        if value == "audio":
            self.settings.type = "audio"
        elif value == "video":
            self.settings.type = "video"
