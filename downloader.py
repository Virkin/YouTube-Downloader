import os
import subprocess

from pytube import Playlist, YouTube
from moviepy.video.io.VideoFileClip import AudioFileClip
from pathlib import Path

def run(pl):
    Path("mp4").mkdir(parents=True, exist_ok=True)
    Path("mp3").mkdir(parents=True, exist_ok=True)

    minVid = 250
    maxVid = 500

    cpt = minVid+1   

    for url in pl.video_urls[minVid:maxVid]:

        try: 

            yt = YouTube(url)

            music =  yt.streams.filter(only_audio=True).first()

            default_filename = "mp4/" + music.default_filename
            
            print("Downloading " + default_filename + "...")
            music.download("mp4/")

            new_filename = "mp3/" + str(cpt) + "-" + default_filename[4:-3] + "mp3"
            
            print("Converting to mp3....")
            clip = AudioFileClip(default_filename)
            clip.write_audiofile(new_filename)
            clip.close()

        except  :
            continue

        cpt += 1

    
    print("Download finished.")

if __name__ == "__main__":
    url = "https://www.youtube.com/playlist?list=PLtjx4SDWorUUS97oSl_gdDyBMoVSDxJXT"
    pl = Playlist(url)
    run(pl)