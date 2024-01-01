import os

from pyrogram import Client 
from pyrogram.filters import me, private, command
from pyrogram.types import Message

from aiohttp import ClientSession
from aiofiles import open
from youtube_search import YoutubeSearch
import yt_dlp

YDL_OPTIONS = {'format': 'bestaudio[ext=m4a]'}


@Client.on_message(
    command(
        commands=['music'],
        prefixes=['.', '/']
    ) & (me | private)
)
async def download_and_send_song(_: Client, message: Message):
    query = ' '.join(message.command[1:])
    msg = await message.reply('**🔎 Finding song...**')
    
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]['title'][:40]
        thumbnail = results[0]['thumbnails'][0]
        thumb_name = f'{title}.jpg'
        
        async with ClientSession() as session:
            async with session.get(thumbnail, allow_redirects=True) as response:
                thumb = await response.read()
        
            async with open(thumb_name, 'wb') as f:
                await f.write(thumb)
        
        duration = results[0]['duration']

    except Exception as e:
        await msg.edit(
            '''
**❌ Song not found.\n\nPlease give a valid song name.**\n\nIf bot don't work, write me @ShadowRazea
            '''.strip()
        )
        print(str(e))
        return
    await msg.edit('**📥 Downloading file...**')

    try:
        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.cache.remove()

            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)


        rep = '<b>🎧 Uploader @ShadowRazea</b>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60

        await msg.edit('**📤 Uploading file...**')
        await message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            title=title,
            duration=dur,
        )
        
        await msg.delete()
    except Exception as e:
        await msg.edit(
            '''
<b>❌ Error, write to owner @ShadowRazea or add issue on \
<a href="https://github.com/shadowrezi/just-userbot">GitHub Repository</a>
</b>
'''.strip()
        )
        print(e)

    finally:
        if os.path.isfile(thumb_name):
            os.remove(thumb_name)
        if os.path.isfile(audio_file):
            os.remove(audio_file)

    print(audio_file)
    print(thumb_name)

