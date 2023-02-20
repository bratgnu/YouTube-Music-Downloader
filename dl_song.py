from pytube import YouTube
import os
from pathlib import Path
from dl_folder import DOWNLOAD_FOLDER

def download_song(link):
    yt = YouTube(link)
        # showing details
    print("Downloading...")
    print("Title: ", yt.title)
    print("Length of video: ", yt.length, " seconds")
        # Extract audio with 160kbps quality from video
    video = yt.streams.filter(abr='160kbps').last()
        # Download the file
    out_file = video.download(output_path=DOWNLOAD_FOLDER)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp3')
    os.rename(out_file, new_file)
    print("Download completed!")
