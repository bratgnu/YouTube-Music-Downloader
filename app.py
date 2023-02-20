from pytube import YouTube
import os
from pathlib import Path
from helpfile import DOWNLOAD_FOLDER

# ask for the link from user
link = input("Enter the link of YouTube video you want to download: ")
yt = YouTube(link)

# showing details
print("Title: ", yt.title)
print("Length of video: ", yt.length, " seconds")

# Extract audio with 160kbps quality from video
print("Downloading...")
video = yt.streams.filter(abr='160kbps').last()

# Downloadthe file
out_file = video.download(output_path=DOWNLOAD_FOLDER)
base, ext = os.path.splitext(out_file)
new_file = Path(f'{base}.mp3')
os.rename(out_file, new_file)
print("Download completed!!")
