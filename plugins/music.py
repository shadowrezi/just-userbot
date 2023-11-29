import requests
import os

from pyrogram import Client, filters

from youtube_search import YoutubeSearch
import yt_dlp


@Client.on_message(
    filters.command(
        commands=['music'],
        prefixes=['.', '/']
    )# & filters.me
)
async def song(_, message):
    query = ' '.join(message.command[1:])
    m = await message.reply('**🔎 Finding song...**')
    ydl_ops = {'format': 'bestaudio[ext=m4a]'}
    
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]['title'][:40]
        thumbnail = results[0]['thumbnails'][0]
        thumb_name = f'{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        
        open(thumb_name, 'wb').write(thumb.content)
        
        duration = results[0]['duration']

    except Exception as e:
        await m.edit(
            '''
**❌ Song not found.\n\nPlease give a valid song name.**\n\nIf bot don't work, write me @ShadowRazea
            '''.strip()
        )
        print(str(e))
        return
    await m.edit('**📥 Downloading file...**')

    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = '''
<b>🎧 Uploader @ShadowRazea
This bot is uploaded on my \
<a href='https://github.com/shadowrezi/just-userbot'>GitHub</a>
</b>
'''.strip()
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60

        await m.edit('**📤 Uploading file...**')
        await message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            title=title,
            duration=dur,
        )
        
        await m.delete()
    except Exception as e:
        await m.edit(
            '''
<b>❌ Error, write to owner @ShadowRazea or add issue on \
<a href="https://github.com/shadowrezi/just-userbot">GitHub Repository</a>
</b>
'''.strip()
        )
        print(e)

    finally:
        os.remove(audio_file)
        os.remove(thumb_name)

    print(audio_file)
    print(thumb_name)
