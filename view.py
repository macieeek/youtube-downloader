import tkinter as tk
from pages.main_panel_page import MainPanelPage
from pages.settings_page import SettingsPage
from pages.statistics_page import StatisticsPage
from settings import Settings

selected_tab = 1


class MainView(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.settings = Settings()
        self.main_panel_page = MainPanelPage(self.settings)
        self.settings_page = SettingsPage(self.settings)
        self.statistics_page = StatisticsPage()

        self.initialize_tabs_bar()
        self.initialize_content()

        self.main_panel_page.show()

    def initialize_tabs_bar(self):
        tabs_bar = tk.Frame(self)
        tabs_bar.pack(side="top", fill="x", expand=False)

        global selected_tab
        selected_tab = tk.IntVar()
        selected_tab.set(1)
        open_main_panel_button = tk.Radiobutton(tabs_bar, variable=selected_tab, value=1, text="Panel główny", command=self.main_panel_page.show, indicatoron=False)
        open_settings_button = tk.Radiobutton(tabs_bar, variable=selected_tab, value=2, text="Ustawienia", command=self.settings_page.show, indicatoron=False)
        open_statistics_button = tk.Radiobutton(tabs_bar, variable=selected_tab, value=3, text="Statystyki", command=self.statistics_page.show, indicatoron=False)

        open_main_panel_button.pack(side="left")
        open_settings_button.pack(side="left")
        open_statistics_button.pack(side="left")

    def initialize_content(self):
        content = tk.Frame(self)
        content.pack(side="top", fill="both", expand=True)

        self.main_panel_page.place(in_=content, x=0, y=0, relwidth=1, relheight=1)
        self.settings_page.place(in_=content, x=0, y=0, relwidth=1, relheight=1)
        self.statistics_page.place(in_=content, x=0, y=0, relwidth=1, relheight=1)

    def handle_close_event(self):
        self.settings.save_settings()
