# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:12:07 2020

@author: DS
"""
"""
Example of WebScrapping using python
"""
from selenium import webdriver
import time 
import youtube_dl 
import os

ydl_opts = {} 

def vidstrip(playlist):
    for i in range(len(playlist)):
        end=playlist[i].find("&")
        playlist[i]=playlist[i][:end]
    return playlist
    
url = input("Enter youtube playlist link : ")
driver = webdriver.Chrome() 
driver.get(url)
time.sleep(5)
playlist=[]
videos=driver.find_elements_by_class_name('style-scope ytd-playlist-video-renderer')
for video in videos:
    link=video.find_element_by_xpath('.//*[@id="content"]/a').get_attribute("href")
    playlist.append(link)
    
vidlist=vidstrip(playlist)
count=1
os.chdir('C:/Users/Trideep/Downloads') 

for link in vidlist:
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except:
        print("Exception occured. Either the video has no quality as set by you, or it is not available. Skipping video {number}".format(number = count))
        continue
    count += 1

driver.close()