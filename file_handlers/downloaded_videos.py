import os
import json
from helper import Helper


class DownloadedVideos:
    def __init__(self):
        self.helper = Helper()

    def get_downloaded_videos(self):
        self.check_if_downloaded_videos_file_is_created()

        return json.load(open(self.helper.get_downloaded_videos_file_path()))

    def check_if_downloaded_videos_file_is_created(self):
        if os.path.exists(self.helper.get_appdata_project_folder_path()) is False:
            folder = "YoutubeDownloader"
            create_path = os.path.join(os.getenv('APPDATA'), folder)
            os.mkdir(create_path)

        if os.path.exists(self.helper.get_appdata_project_folder_path()) and os.path.exists(self.helper.get_downloaded_videos_file_path()) is False:
            filename = "downloaded_videos.json"
            with open(os.path.join(self.helper.get_appdata_project_folder_path(), filename), "w") as downloaded_videos_file:
                self.create_default_downloaded_videos_file(downloaded_videos_file)

        if os.stat(self.helper.get_downloaded_videos_file_path()).st_size == 0:
            with open(self.helper.get_downloaded_videos_file_path(), "w") as downloaded_videos_file:
                self.create_default_downloaded_videos_file(downloaded_videos_file)

    @staticmethod
    def create_default_downloaded_videos_file(downloaded_videos_file):
        data = {}
        downloaded_videos_file.write(json.dumps(data))

    def save_new_downloaded_video_info(self, video_info_dict):
        self.check_if_downloaded_videos_file_is_created()

        index_of_downloaded_video = 0
        all_downloaded_videos_dict = {}
        # file with downloaded videos info is not empty
        if os.path.getsize(self.helper.get_downloaded_videos_file_path()) != 0:
            downloaded_videos_dict = json.load(open(self.helper.get_downloaded_videos_file_path()))
            for index, value in downloaded_videos_dict.items():
                all_downloaded_videos_dict[index] = value
                index_of_downloaded_video = index
            index_of_downloaded_video = int(index_of_downloaded_video) + 1

        all_downloaded_videos_dict[str(index_of_downloaded_video)] = video_info_dict

        with open(self.helper.get_downloaded_videos_file_path(), "w") as downloaded_videos_file:
            downloaded_videos_file.write(json.dumps(all_downloaded_videos_dict, indent=4, sort_keys=True, default=str))
