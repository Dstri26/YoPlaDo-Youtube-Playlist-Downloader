# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:12:07 2020

@author: DS
"""
"""
Example of WebScrapping using python
"""
from pytube import YouTube
import bs4
import requests



playlist=[]
url=input("Enter the Youtube Playlist URL : ") #Takes the Playlist Link
try:
    data = requests.get(url)
except:
    print("An exception occured while downloading the playlist. Error: Unable to fetch data from the error or the link is not valid.")
    exit()
soup=bs4.BeautifulSoup(data.text,'html.parser')


for links in soup.find_all('a'):
        link=links.get('href')
        if (link[0:6]=="/watch" and link[0]!="#"):
            link="https://www.youtube.com"+link
            link=str(link)
            playlist.append(link)
del playlist[0:2]

count = 1

playlist = sorted(set(playlist), key = playlist.index)

vquality=input("Enter the video quality (1080,720,480,360,240,144):")
vquality=vquality+"p"

for link in playlist:
    try:
        yt = YouTube(link)
        videos= yt.streams.filter(mime_type="video/mp4",res=vquality)
        video = videos[0]
    except:
        print("Exception occured. Either the video has no quality as set by you, or it is not available. Skipping video {number}".format(number = count))
        count += 1
        continue

    video.download("Downloads")
    print(yt.title+" - has been downloaded !!!")
    count += 1

