# I am designing a code which takes the websites from a youtube playlist, and will tell the total run time.

from bs4 import BeautifulSoup
import urllib2
import json             #for prev code
import urllib           #for prev code

import re

from datetime import timedelta
from urllib2 import urlopen
from xml.dom.minidom import parseString



def gettime(urlx)

    #get urls
    html_page = urllib2.urlopen("http://gdata.youtube.com/feeds/api/playlists/PL-42LlEWDC8qyW-zJnzPKRjxYVX4QsrJ1")
    soup = BeautifulSoup(urlx)
    linkx = []
    for i in soup.find_all('link'):
        if "watch" in i['href']:
            linkx.append(i)
'''
    urlcut=urlx.split
    video_id = urlcut[1]
    api_key = "AIzaSyD2YHDzYYxNQL-g9_6cZWMu5Fe5VgfiXOc"
    searchUrl = "https://www.googleapis.com/youtube/v3/videos?id=" + video_id + "&key=" + api_key + "&part=contentDetails"
    response = urllib.urlopen(searchUrl).read()
    data = json.loads(response)
    all_data = data['items']
    contentDetails = all_data[0]['contentDetails']
    duration = contentDetails['duration']
    intermediate1=duration.split('M')
    inter1 = intermediate1[0]
    intermediate2=inter1.split('PT')
    min = repr(intermediate2)
    inter2=intermediate1[1]
    intermediate3=inter2.split('S')
    sec = repr(intermediate3)
    totalinseconds = min*60 + sec
'''

    #get time
    for vid in linkx:
        url = 'https://gdata.youtube.com/feeds/api/videos/{0}?v=2'.format(vid)
        s = urlopen(url).read()
        d = parseString(s)
        e = d.getElementsByTagName('yt:duration')[0]
        a = e.attributes['seconds']
        v = int(a.value)
        t = timedelta(seconds=v)
        print(t)


gettime('https://www.youtube.com/watch?v=rExcQ5nm_yU&list=PUIvxmYZSfLNbtA4OPMHqKBw')

