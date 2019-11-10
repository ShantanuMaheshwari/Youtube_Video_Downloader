#!/usr/bin/python3
"""This script uses youtube-dl to download youtube video
Till now it only supports single videos instead of playlist"""

import os


class YoutubeVideoDownloader:

    def __init__(self):
        self.mode = input("Enter 1 for single video mode or 2 for batch mode: ")
        self.youtube_video_url = ''
        self.youtube_video_title = ''
        self.video_format = ''
        self.audio_format = ''
        if self.mode == '1':
            self.download_video()
        elif self.mode == '2':
            youtube_file = input("Enter file name containing links title and formats: ")
            file = open(youtube_file, 'r')
            file_data = file.read().split('\n')[:-1]
            line_number = 0
            while line_number < len(file_data):
                self.set_youtube_video_url(file_data[line_number])
                line_number += 1
                self.set_youtube_video_title(file_data[line_number])
                line_number += 1
                self.set_video_audio_quality(file_data[line_number])
                line_number += 1
                self.download_video()

    def set_youtube_video_url(self, url):
        if self.mode == '1':
            self.youtube_video_url = " " + input("Enter youtube video url: ").split("&list")[0]
        elif self.mode == '2':
            self.youtube_video_url = " " + url.split("&list")[0]

    def set_youtube_video_title(self, title):
        if self.mode == '1':
            self.youtube_video_title = "\"" + input("Enter video title: ") + ".%(ext)s\""
        elif self.mode == '2':
            self.youtube_video_title = "\"" + title + ".%(ext)s\""
        return self.youtube_video_title

    def set_video_audio_quality(self, quality):
        if self.mode == '1':
            print("Enter video and audio formats(Press 0 for best quality): ")
            self.video_format, self.audio_format = input().split()
        if self.mode == '2':
            self.video_format, self.audio_format = quality.split()
        return self.video_format, self.audio_format

    def download_video(self):
        # Downloading single videos instead of playlist so adding .split("&list")
        if self.mode == '1':
            self.set_youtube_video_url(0)
            self.set_youtube_video_title(0)
            print("---------------------Available Formats------------------------ ")
            # Terminal command for displaying available audio and video formats
            os.system("youtube-dl -F" + self.youtube_video_url)
            self.set_video_audio_quality(0)
        print(self.youtube_video_title)
        if self.video_format == '0':
            self.video_format = "bestvideo"
        if self.audio_format == '0':
            self.audio_format = "bestaudio"
        # Terminal command for downloading videos
        os.system(''.join(["youtube-dl -o ", self.youtube_video_title,
                           " -f ", self.video_format, "+", self.audio_format,
                           self.youtube_video_url]))


if __name__ == '__main__':
    YoutubeVideoDownloader()
