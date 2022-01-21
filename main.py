import tkinter as tk
from view import MainView


# save settings before close application
def handle_close_event(window, main_view):
    main_view.handle_close_event()
    window.destroy()


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

    window.protocol("WM_DELETE_WINDOW", lambda: handle_close_event(window, main_view))
    window.mainloop()


if __name__ == "__main__":
    main()