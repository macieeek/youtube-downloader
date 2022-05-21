# YouTube Downloader

> ### Project of the dekstop application which allows to download videos or even just sound from YouTube.

- The whole application is made in [python](https://www.python.org/downloads/).
- GUI is made with [tkinter](https://docs.python.org/3/library/tkinter.html).
- To handle actions related with downloading video is used [pytube](https://pytube.io/en/latest/).

# Installation

To successfully install application you need to have installed [python](https://www.python.org/downloads/) and [pip](https://pypi.org/project/pip/).

Open folder where you want to have project files, open console and then clone the repository

    git clone https://github.com/maciekiwaniuk/youtube-downloader
	
Change folder in console to created folder with project files

	cd youtube-downloader

Install all the required modules using pip

    pip install -r requirements.txt

In case of any problems with pytube library I suggest to upgrade package to newest version

    pip install --upgrade pytube

Run application

    py main.py

# Application usage

To successfully download video from YouTube you need to enter the URL of video and click download. 
You can configure the specifications of videos in the settings tab.

# Application appearance

![](https://github.com/maciekiwaniuk/youtube-downloader/raw/main/assets/image_1.png?raw=true)
![](https://github.com/maciekiwaniuk/youtube-downloader/raw/main/assets/image_2.png?raw=true)