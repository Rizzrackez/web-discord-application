import time
import os

import youtube_dl
import transliterate


def convert_youtube(youtube_link):

    ydl_opts = {
        'noplaylist': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url=youtube_link, download=False)
        result_str = info_dict["title"]
        try:
            result_str = transliterate.translit(result_str, reversed=True)
        except:
            pass

    ytb_name = result_str

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'music/{ytb_name}.m4a',  # имя и формат создаваемого аудиофайла
        'noplaylist': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if not os.path.isfile(f'music/{ytb_name}.m4a'):
            # info_dict = ydl.extract_info(youtube_link, download=False)
            ydl.download([youtube_link])

    return ytb_name
