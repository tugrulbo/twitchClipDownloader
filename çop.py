from twitch import TwitchClient
from twitchdl import exceptions, download
import os
import glob
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
#def getURLsOwner():
#    f = open("../TWITCHCLIPDOWNLOADER/ownerurls.txt","w")
#    client = TwitchClient(client_id="nn7vv9k6ulqrjutmthwys0ew2epic5",oauth_token="uwhsyzgiy08i40tsc620l6uejd96ds")
#    liste = client.clips.get_top(game="Valorant",period="day",limit=10,trending=False)
#    for i in range(0,len(liste)):
#        if(i < len(liste)):
#            print("İsim Gösterim Şekli: {} --- URL: {}".format(liste[i]["broadcaster"]["display_name"],liste[i]["broadcaster"]["channel_url"]))
#            url = liste[i]["broadcaster"]["channel_url"]
#            video = liste[i]["url"]
#            print(video)
#            f.write(url+"\n")
#    f.close()
#getURLsOwner()

def readClipsFile():
    arr = os.listdir('../Twitchclipdownloader/*.mp4')
    print(arr)


def readClip():
    liste = []
    for file_name in glob.iglob('*.mp4', recursive=True):
        liste.append(file_name)
    
    return liste

readClip()

def mergeClips():
    videoFileNames = readClip()
    clips = []
    for i in range(0,len(videoFileNames)):
        clips.append(VideoFileClip(videoFileNames[i]))

    print(clips)
    result = CompositeVideoClip([clips[0],clips[1],clips[2]])
    result.write_videofile("mergedNew.mp4",fps=60)

mergeClips()