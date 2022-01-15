import tkinter as tk
from tkinter import ttk
from pages.main_panel_page import MainPanelPage
from pages.settings_page import SettingsPage
from pages.statistics_page import StatisticsPage


class MainView(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.main_panel_page = MainPanelPage()
        self.settings_page = SettingsPage()
        self.statistics_page = StatisticsPage()

        self.initialize_tabs_bar()
        self.initialize_content()

        self.main_panel_page.show()

    def initialize_tabs_bar(self):
        tabs_bar = tk.Frame(self)
        tabs_bar.pack(side="top", fill="x", expand=False)

        open_main_panel_button = tk.Button(tabs_bar, text="Panel główny", command=self.main_panel_page.show)
        open_settings_button = tk.Button(tabs_bar, text="Ustawienia", command=self.settings_page.show)
        open_statistics_button = tk.Button(tabs_bar, text="Statystyki", command=self.statistics_page.show)

        open_main_panel_button.pack(side="left")
        open_settings_button.pack(side="left")
        open_statistics_button.pack(side="left")

    def initialize_content(self):
        content = tk.Frame(self)
        content.pack(side="top", fill="both", expand=True)

        self.main_panel_page.place(in_=content, x=0, y=0, relwidth=1, relheight=1)
        self.settings_page.place(in_=content, x=0, y=0, relwidth=1, relheight=1)
        self.statistics_page.place(in_=content, x=0, y=0, relwidth=1, relheight=1)