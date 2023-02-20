# import packages
from pytube import YouTube

# This function checks if a given link contains a whole playlist, or just one video
def check_youtube_link(link):
    if "playlist" in link:
        return "playlist"
    else:
        try:
            YouTube(link)
            return "video"
        except:
            return "invalid"
