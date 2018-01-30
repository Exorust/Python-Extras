#chandu's youtube-dl
from bs4 import BeautifulSoup
import requests
import pafy
links=[]
name=''

def playlist_rip(url):
    results= requests.get(url)
    ht=results.content
    soup=BeautifulSoup(ht, 'lxml')
    for htmlrip in soup.findAll('li', {'class': 'yt-uix-scroller-scroll-unit '}):
        link="https://www.youtube.com/watch?v="+htmlrip.get('data-video-id')
        links.append(link)
        continue


urlx='https://www.youtube.com/watch?v=JcSjjAqzPBA&list=PLecj36ttAZK4siCStayp5edewxlOD666b'
playlist_rip(urlx)
for link in links:
    video = pafy.new(link)
    best = video.getbest()
    print("Size is %s" % best.get_filesize())
    file = best.download()
