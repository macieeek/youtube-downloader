import os
import json
from helper import Helper


class Settings:
    def __init__(self):
        self.helper = Helper()

        settings = self.get_settings()

        self.type = settings["type"]
        self.resolution = settings["resolution"]
        self.extension = settings["extension"]
        self.directory = settings["directory"]
        self.custom_directory_path = settings["custom_directory_path"]

    def get_settings(self):
        self.check_if_settings_file_is_created()

        return json.load(open(self.helper.get_settings_file_path()))

    def check_if_settings_file_is_created(self):
        if os.path.exists(self.helper.get_appdata_project_folder_path()) is False:
            folder = "YoutubeDownloader"
            create_path = os.path.join(os.getenv('APPDATA'), folder)
            os.mkdir(create_path)

        if os.path.exists(self.helper.get_appdata_project_folder_path()) and os.path.exists(self.helper.get_settings_file_path()) is False:
            filename = "settings.json"
            with open(os.path.join(self.helper.get_appdata_project_folder_path(), filename), "w") as settings_file:
                self.create_default_settings_file(settings_file)

    def create_default_settings_file(self, settings_file):
        data = {}
        data["type"] = "video"
        data["resolution"] = "highest"
        data["extension"] = "mp4"
        data["directory"] = "desktop"
        data["custom_directory_path"] = self.helper.get_desktop_path()

        settings_file.write(json.dumps(data))

    def save_settings(self):
        data = {}
        data["type"] = self.type
        data["resolution"] = self.resolution
        data["extension"] = self.extension
        data["directory"] = self.directory
        data["custom_directory_path"] = self.custom_directory_path

        with open(self.helper.get_settings_file_path(), "w") as settings_file:
            settings_file.write(json.dumps(data))


