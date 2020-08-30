from twitch import TwitchClient
from twitchdl import exceptions, download
import youtube_dl as yt
import youtube_dl
from youtube_search import YoutubeSearch
import asyncio
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip


def getURLs():
    f = open("../TWITCHCLIPDOWNLOADER/videourls.txt","w")
    client = TwitchClient(client_id="nn7vv9k6ulqrjutmthwys0ew2epic5",oauth_token="uwhsyzgiy08i40tsc620l6uejd96ds")
    liste = client.clips.get_top(game="Valorant",period="day",limit=3,trending=False)
    for i in range(0,len(liste)):
        print("İzlenme Sayisi: {} --- URL: {}".format(liste[i]["views"],liste[i]["url"]))
        url = liste[i]["url"]
        f.write(url+"\n")
    f.close()
getURLs()



def blacklistCheck():
    r = open("../TWITCHCLIPDOWNLOADER/videourls.txt","r")
    b = open("../TWITCHCLIPDOWNLOADER/blacklist.txt","r")
    new_list = []
    url_list = r.readlines()
    blacklist_url = b.readlines()
    for i in range(0,3):
        if len(blacklist_url) == 0:
            new_list.append(url_list[i])
        elif len(blacklist_url)>0:
            for j in range(0,len(blacklist_url)): 
                if blacklist_url[j] != url_list[i]:
                    new_list.append(url_list[i])
                else:
                    print("Blacklist URL bulundu: {}".format(blacklist_url[j]))
    
    r.close()
    b.close()
    return new_list
new_list = blacklistCheck()
print(new_list)

def downloadVideos(liste):
    ytdl_format_options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
    }

    ffmpeg_options = {
        'options': '-vn'
    }

    ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


    class YTDLSource():
        def __init__(self, source, *, data, volume=0.5):
            super().__init__(source, volume)

            self.data = data

            self.title = data.get('title')
            self.url = data.get('url')

        @classmethod
        async def from_url(cls, url, *, loop=None, stream=False):
            loop = loop or asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

            if 'entries' in data:
                # take first item from a playlist
                data = data['entries'][0]

            filename = data['url'] if stream else ytdl.prepare_filename(data)
        
    for i in range(0,3):
        asyncio.run(YTDLSource.from_url(liste[i], stream=False))
               
downloadVideos(new_list)
def readClip():
    liste = []
    for file_name in glob.iglob('*.mp4', recursive=True):
        liste.append(file_name)
    
    return liste

readClip()


