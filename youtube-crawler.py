#This program will start from a given video and find the linking of other users to it
import requests
from bs4 import BeautifulSoup
userdict={}


def youtube_crawler(url):
    while True:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        # update count
        for link in soup.findAll('a', {'class': 'g-hovercard'}):
            x = link.string
            if x in userdict:
                userdict[x] =userdict[x]+ 1
            else:
                userdict[x] = 1
        # update current video
        for link in soup.findAll('a', {'class': "g-hovercard yt-uix-sessionlink      spf-link "}):
            y = link.string
            if y in userdict:
                userdict[x] =userdict[x]+ 1
            else:
                userdict[x] = 1
        # print values
        print(userdict)
        # goto next video
        for link in soup.findAll('a', {'class': " content-link spf-link  yt-uix-sessionlink       spf-link "}):
            href = 'https://www.youtube.com' + link.get('href')
            url = href




youtube_crawler('https://www.youtube.com/watch?v=oWA4TddxXG4')


