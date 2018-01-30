# This program will find total time of all videos in a given directory
import os
from moviepy.editor import VideoFileClip
path = '/home/chandrahas/Downloads/x'
lists = os.listdir(path)

for l in lists:
    clip = VideoFileClip(path+'/'+l)
    total =+ clip.duration
print(total)

