import os
import json
from helper import Helper


class Settings:
    def __init__(self):
        self.helper = Helper()

        settings = self.get_settings()

        self.directory = settings["directory"]
        self.extension = settings["extension"]
        self.resolution = settings["resolution"]

    def get_settings(self):
        self.check_if_settings_file_is_created()

        return json.load(open(self.helper.get_settings_file_path()))

    def check_if_settings_file_is_created(self):
        if os.path.exists(self.helper.get_settings_folder_path()) is False:
            folder = "YoutubeDownloader"
            create_path = os.path.join(os.getenv('APPDATA'), folder)
            os.mkdir(create_path)

        if os.path.exists(self.helper.get_settings_folder_path()) and os.path.exists(self.helper.get_settings_file_path()) is False:
            filename = "settings.json"
            with open(os.path.join(self.helper.get_settings_folder_path(), filename), "w") as settings_file:
                self.create_default_settings_file(settings_file)


    def create_default_settings_file(self, settings_file):
        data = {}
        data["extension"] = "mp4"
        data["resolution"] = "lowest"
        data["directory"] = self.helper.get_download_path()

        settings_file.write(json.dumps(data))


