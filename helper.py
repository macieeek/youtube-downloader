import os
import requests


class Helper:
    def __init__(self):
        pass

    @staticmethod
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

    @staticmethod
    def get_desktop_path():
        return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    @staticmethod
    def get_settings_folder_path():
        return f"{os.getenv('APPDATA')}/YoutubeDownloader"

    @staticmethod
    def get_settings_file_path():
        return f"{os.getenv('APPDATA')}/YoutubeDownloader/settings.json"

    @staticmethod
    def check_internet_connection():
        url = "https://youtube.com"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            return True
        except:
            return False