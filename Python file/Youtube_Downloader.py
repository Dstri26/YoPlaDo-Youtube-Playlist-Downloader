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
from pytube import YouTube as yt
import os
from selenium.webdriver.chrome.options import Options  

ydl_opts = {} 
playlist=[]    
url = input("Enter youtube playlist link : ")

if url.find('playlist?list=')!=-1:
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  

    driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
    driver.get(url)
    time.sleep(5)

    videos=driver.find_elements_by_id('video-title')
    for video in videos:
        link=video.get_attribute("href")
        end=link.find("&")
        link=link[:end]
        playlist.append(link)
    driver.close()

elif url.find('watch?v=')!=-1:
    playlist.append(url)

os.chdir('C:/Users/Trideep/Downloads') 

for link in playlist:
    vid=yt(link)
    print("--------------------------------")
    print(vid.title+" is being downloaded !!")
    vid.streams.get_highest_resolution().download()
    print(vid.title+" has been successfully downloaded !!")
    print("--------------------------------")
