import os
from pytube import YouTube


# Return path to download folder
def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


def main():
    url_to_video = input("Pass url to youtube video: ")

    video = YouTube(url_to_video)

    print(f"Downloading video... ")
    video.streams.get_highest_resolution().download(get_download_path())
    print(f"Video with title \"{video.title}\" has been downloaded.")


if __name__ == "__main__":
    main()