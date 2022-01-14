import tkinter as tk
from view import MainView


def main():
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x600")
    root.mainloop()

    # url_to_video = input("Pass url to youtube video: ")
    # video = YouTube(url_to_video)
    # print(f"Downloading video... ")
    # video.streams.get_highest_resolution().download(get_download_path())
    # print(f"Video with title \"{video.title}\" has been downloaded.")


if __name__ == "__main__":
    main()