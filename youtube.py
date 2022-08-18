import re
import os
import time
import webbrowser
import tkinter as tk
import urllib.request
from py_youtube import Data
os.system('cls')
n = 0
while True:
    duration = 5
    x = input('Enter the video you want to see: ')
    y = int(input('Enter number of videos: '))
    x = x.replace(' ','+')
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+x)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_ids = list(set(video_ids))
    all = len(video_ids)
    if y > all:
        y = all
    print('Videos:\n')
    all = []
    for i in range(0,y):
        n = n + 1
        data = Data("https://youtu.be/"+video_ids[i]).data()
        all.append("https://youtu.be/"+video_ids[i])
        print(str(n)+'. '+data['title']+'|'+str(data['channel_name']))
    print()
    num = int(input('Enter the number of the video you want: '))
    num = num - 1
    print('This is what you want to see')
    data = Data(all[num]).data()
    print(data['title']+'|'+str(data['channel_name'])+'\n'+'Subscribers: '+str(data['subscriber'])+'\n'+'Likes: '+str(data['likes'])+'\n'+'Views: '+str(data['views'])+'\nDate: '+str(data['publishdate']))
    try:
        import pafy
        print('Duration:',pafy.new("http://www.youtube.com/watch?v="+video_ids[num]).length)
    except:
        pass
    x = input('Would you like to open it 1.Yes 2.No: ')
    if x == '2':
        os.system('cls')
        n = 0
        continue
    else:
        pass
    print('Opening video')
    webbrowser.open('https://www.youtube.com/embed/'+video_ids[num])
    os.system('cls')
    choice = input('Enter if you want transcript and sound 1.Yes 2.No: ')
    if choice == '1':
        try:
            from youtube_transcript_api import YouTubeTranscriptApi
            trans = YouTubeTranscriptApi.get_transcript(video_ids[num])
            a = 1
            string = ''
            for i in trans:
                if a % 5 == 0:
                    print(i['text'])
                else:
                    print(i['text'],end = ' ')
        except:
            print('Subtitles unavailble')
    else:
        pass
    print()
    next = input('Enter if you want recemendations 1.yes 2.No ')
    if next == '2':
        os.system('cls')
        n = 0
        continue
    import recemendation
    print('Recemdations\n')
    print(recemendation.allofit(video_ids[num]))
    enter = input('')
    os.system('cls')
    n = 0
