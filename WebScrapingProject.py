# downloads wallpaper images and puts them into a new folder
import requests
import re
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import wget
import os

url = "https://wallpapercave.com/rain-wallpaper-hd"
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(req).read()
#parse html
page_soup = soup(webpage, "html.parser")
#get all of the image urls
images = page_soup.find_all("img", {"src": re.compile(".jpg")})
#pop off the first image
images.pop(0)
#create a list to store our urls
urls = []
#create directory
dirName = "rainPictures" + str(1);
#if directory doesint exist create it
try:
    os.mkdir(dirName)
    print("Directory ",dirName,"is Created!")
except FileExistsError:
    print("Directory ",dirName," already exists!")
#shove our urls into a list
for image in images:
    urls.append(url[:25] + image["src"])
#check wether or not user is ok with downloading images to this file
print("are you read to download all images from " + url + "?")
yes_or_no = input()
if yes_or_no == "yes":
    for i in urls:
     wget.download(i,dirName)

