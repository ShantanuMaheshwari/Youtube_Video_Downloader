#!/usr/bin/python3
"""This script uses youtube-dl to download youtube video
Till now it only supports single videos instead of playlist"""

import os


def download_video():
    # os.chdir("/home/shantanu/Videos/Youtube_Videos")
    directory = input("Enter directory for video to be saved(Press 0 for current directory): ")
    if directory != '0':
        if not os.path.exists(directory):
            os.makedirs(directory)
        os.chdir(directory)
    # Downloading single videos instead of playlist so adding .split("&list")
    video_url = " " + input("Enter youtube video url: ").split("&list")[0]
    video_title = "\"" + input("Enter video title: ") + ".%(ext)s\""
    print("---------------------Available Formats------------------------ ")
    # Terminal command for displaying available audio and video formats
    os.system("youtube-dl -F" + video_url)
    video_format, audio_format = input("Enter video and audio formats(Press 0 for best quality): ").split()
    if video_format == '0':
        video_format = "bestvideo"
    if audio_format == '0':
        audio_format = "bestaudio"
    # Terminal command for downloading videos
    os.system(''.join(["youtube-dl -o ", video_title, " -f ", video_format, "+", audio_format, video_url]))


if __name__ == '__main__':
    download_video()
