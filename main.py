import tkinter as tk
from view import MainView


def main():
    window = tk.Tk()

    window_width = 514
    screen_width = window.winfo_screenwidth()
    x = (screen_width / 2) - (window_width / 2)

    window_height = 400
    screen_height = window.winfo_screenheight()
    y = (screen_height / 2) - (window_height / 2)

    window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
    window.title("YouTube Downloader")
    window.resizable(False, False)

    main_view = MainView(window)
    main_view.pack(side="top", fill="both", expand=True)

    window.mainloop()




if __name__ == "__main__":
    main()