import tkinter as tk
from pages.main_panel_page import MainPanelPage
from pages.settings_page import SettingsPage
from pages.statistics_page import StatisticsPage


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        main_panel_page = MainPanelPage(self)
        settings_page = SettingsPage(self)
        statistics_page = StatisticsPage(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        main_panel_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        settings_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        statistics_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Panel główny", command=main_panel_page.show)
        b2 = tk.Button(buttonframe, text="Ustawienia", command=settings_page.show)
        b3 = tk.Button(buttonframe, text="Statystyki", command=statistics_page.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        main_panel_page.show()