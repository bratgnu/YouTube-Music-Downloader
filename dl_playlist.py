# importing packages
from pytube import Playlist, YouTube
import os
from pathlib import Path
from dl_folder import DOWNLOAD_FOLDER

def download_playlist(link):
    playlist = Playlist(link)
        # showing details of playlist
    print("Number of videos in playlist: ", len(playlist.video_urls))
        # iterate through each video in the playlist and download it
    for video_url in playlist.video_urls:
        try:
            yt = YouTube(video_url)
                # showing details
            print("Downloading: ", yt.title)
                # Extract audio with 160kbps quality from video
            video = yt.streams.filter(abr='160kbps').last()
                # Download the file
            out_file = video.download(output_path=DOWNLOAD_FOLDER)
            base, ext = os.path.splitext(out_file)
            new_file = Path(f'{base}.mp3')
            os.rename(out_file, new_file)
        except:
            print("Error downloading video: ", video_url)
    print("Download completed!")



