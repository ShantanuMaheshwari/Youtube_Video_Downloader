#!/home/shantanu/PythonProjects/Youtube_Downloader/venv/bin/python3

import os
import time
import requests
from bs4 import BeautifulSoup


"""This script uses youtube-dl to download youtube video
Till now it only supports single videos instead of playlist"""
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


if __name__ == '__main__':
    YoutubeVideoDownloader()
