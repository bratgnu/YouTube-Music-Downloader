from pytube import YouTube
from helpfile import DOWNLOAD_FOLDER

# ask for the link from user
link = input("Enter the link of YouTube video you want to download: ")
yt = YouTube(link)

# showing details
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)

# get the highest resolution possible
ys = yt.streams.get_highest_resolution()

# ask for the output folder from user
output_folder = DOWNLOAD_FOLDER

# starting download
print("Downloading...")
ys.download(output_path=output_folder)
print("Download completed!!")
