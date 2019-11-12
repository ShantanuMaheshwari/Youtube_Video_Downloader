#!/home/shantanu/PythonProjects/Youtube_Downloader/venv/bin/python3

import os
import time
import requests
from bs4 import BeautifulSoup
import pyperclip


"""This script uses youtube-dl to download youtube video
Till now this script only supports single videos instead of playlist.
You can add links of videos using create_video_playlist.py and pass that file on this script 
to download multiple videos"""
"""To activate venv go inside bin directory and type 'source ./activate'"""


class YoutubeVideoDownloader:

    def __init__(self):
        self.mode = input("Enter 1 for Single video mode or 2 for Batch mode: ")
        self.youtube_video_url = ''
        self.youtube_video_title = ''
        self.video_format = '0'
        self.audio_format = '0'
        # flag_1 returned from command displaying available formats
        # On success execution of os.system 0 is returned
        self.flag_1 = 0
        # flag_2 returned after downloading video
        self.flag_2 = 0
        if self.mode == '1':
            self.download_video()
        elif self.mode == '2':
            youtube_file = input("Enter file name containing links and title: ")
            file = open(youtube_file, 'r')
            file_data = file.read().split('\n')
            file.close()
            line_number = 0
            while line_number < len(file_data):
                self.set_youtube_video_url(file_data[line_number])
                line_number += 1
                self.set_youtube_video_title()
                line_number += 1
                self.download_video()
                if self.flag_2 == 0:
                    # Deleting url and title of videos downloaded
                    # time.sleep(5)
                    del file_data[line_number - 2:line_number]
                    line_number -= 2
                file = open(youtube_file, 'w')
                file.write('\n'.join(file_data))
                file.close()

    def set_youtube_video_url(self, url):
        self.youtube_video_url = " " + url.split("&list")[0]

    def set_youtube_video_title(self):
        # Using web scraping to find title of the video
        r = requests.get(self.youtube_video_url)
        soup = BeautifulSoup(r.content, 'html5lib')
        title = soup.find('title')
        self.youtube_video_title = "\"" + title.get_text() + ".%(ext)s\""
        print(self.youtube_video_title)

    def set_video_audio_quality(self, quality):
        self.video_format, self.audio_format = quality.split()

    def download_video(self):
        # Downloading single videos instead of playlist so adding .split("&list")
        if self.mode == '1':
            self.set_youtube_video_url(input("Enter youtube video url: "))
            self.set_youtube_video_title()
            print("---------------------Available Formats------------------------ ")
            # Terminal command for displaying available audio and video formats
            self.flag_1 = os.system("youtube-dl -F" + self.youtube_video_url)
            if self.flag_1 != 0:
                print("Invalid youtube video url.")
                exit()
            print("Enter video and audio formats(Press 0 for best quality): ", end='')
            self.set_video_audio_quality(input())
        print(self.youtube_video_title)
        if self.video_format == '0':
            self.video_format = "bestvideo"
        if self.audio_format == '0':
            self.audio_format = "bestaudio"
        # Terminal command for downloading videos
        self.flag_2 = os.system(''.join(["youtube-dl -o ", self.youtube_video_title,
                                         " -f ", self.video_format, "+", self.audio_format,
                                         self.youtube_video_url]))
        print("Status of cmd: ", self.flag_2, '\n')


class CreateVideoPlaylist:
    """pyperclip doesn't work on linux, run commands:
    'sudo apt-get install xsel'  to install the xsel utility.
    'sudo apt-get install xclip' to install the xclip utility.
    """
    def __init__(self):
        url_list = []
        paste = ''
        i = 0

        no_of_links = int(input("Enter number of links to be pasted: "))
        file_name = input('Enter file name: ')
        print("After copying first link press Enter, then copy rest of the links. ")
        print("Links will be pasted in the above file automatically")
        input()

        while i < no_of_links:
            if paste != pyperclip.paste():
                paste = pyperclip.paste()
                url_list.append(paste)
                print(paste)
                i += 1

        file = open(file_name, 'a')
        file.write('\n'.join(url_list))
        file.close()


if __name__ == '__main__':
    print('Mode 0: Create Video playlist')
    print('Mode 1: Download youtube videos: ')
    mode = input('Enter Mode: ')
    if mode == '0':
        CreateVideoPlaylist()
    elif mode == '1':
        YoutubeVideoDownloader()
    else:
        print('Invalid Mode')
