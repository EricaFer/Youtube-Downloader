from pytube import Channel
from pytube import YouTube
import time

# Channel URL
c = Channel('https://www.youtube.com/c/engvidRebecca/videos')
print(f'Downloading videos by: {c.channel_name}')

for url in c.video_urls[:50]:
    try:
        yt = YouTube(url)
        yt.streams\
        .filter(progressive=True, file_extension='mp4')\
        .order_by('resolution')\
        .desc()\
        .first()\
        .download()

    except:
        print(url)
        time.sleep(2)