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
    
url = input("Enter youtube playlist link : ")
chrome_options = Options()  
chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
driver.get(url)
time.sleep(5)
playlist=[]
videos=driver.find_elements_by_id('video-title')
for video in videos:
    link=video.get_attribute("href")
    end=link.find("&")
    link=link[:end]
    playlist.append(link)
os.chdir('C:/Users/Trideep/Downloads') 

for link in playlist:
    print(link)
    vid=yt(link)
    vid.streams.get_highest_resolution().download()
    print(vid.title+" has been successfully downloaded !!")
driver.close()
