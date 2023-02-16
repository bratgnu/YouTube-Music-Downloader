from pytube import YouTube, Playlist
from helpfile import DOWNLOAD_FOLDER

# ask for the link from user
link = input("Enter the link of YouTube playlist you want to download: ")
playlist = Playlist(link)

# ask for the output folder
output_folder = DOWNLOAD_FOLDER

# showing details of playlist
print("Number of videos in playlist: ", len(playlist.video_urls))

# iterate through each video in the playlist and download it
for video_url in playlist.video_urls:
    try:
        yt = YouTube(video_url)
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length)
        print("Rating of video: ", yt.rating)
        # get the highest resolution possible
        ys = yt.streams.get_highest_resolution()

        # starting download
        print("Downloading...")
        ys.download(output_path=output_folder)
        print("Download completed!!")
    except:
        print("Error downloading video: ", video_url)

print("All videos in playlist have been downloaded successfully!")
