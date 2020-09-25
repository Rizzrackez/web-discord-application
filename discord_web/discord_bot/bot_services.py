import time
import os

import youtube_dl


def convert_youtube(youtube_link):

    result_str = str(time.time())
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'music/{result_str}.m4a',  # имя и формат создаваемого аудиофайла
        'noplaylist': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if not os.path.isfile(f'music/{result_str}.m4a'):
            # info_dict = ydl.extract_info(youtube_link, download=False)
            ydl.download([youtube_link])

    return result_str
