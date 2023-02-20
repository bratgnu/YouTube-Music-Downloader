# import packages
from check_yt_link import check_youtube_link
from dl_song import download_song
from dl_playlist import download_playlist

# ask for the link from user
link = input("Enter the link of YouTube video you want to download: ")

# Test output, informing you what type of link was input
link_type = check_youtube_link(link)
if link_type == "playlist":
    download_playlist(link)
elif link_type == "video":
    download_song(link)
else:
    print("Link is invalid")
