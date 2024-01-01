from aiohttp import ClientSession

from pyrogram import Client
from pyrogram.filters import me, private, command
from pyrogram.types import Message

from aiofiles import open
from aiofiles.os import remove, path

from youtube_search import YoutubeSearch
import yt_dlp
from fake_useragent import UserAgent

YDL_OPTIONS = {'format': 'bestaudio[ext=m4a]'}

OWNER = 'ShadowRazea'
CAPTION = f'<b>🎧 Uploader @{OWNER}</b>'
FINDING_SONG = '<b>🔎 Finding song...</b>'
SONG_NOT_FOUND = f"<b>❌ Song not found.\n\nPlease give a valid song name.</b>\n\nIf bot don't work, write me @{OWNER}"
DOWNLOADING_FILE = '<b>📥 Downloading file...</b>'
UPLOADING_FILE = '<b>📤 Uploading file...</b>'
ERROR = f'<b>❌ Error, write to OWNER @{OWNER} or add issue on <a href="https://github.com/shadowrezi/just-userbot">GitHub Repository</a></b>'


async def search_video(query: str) -> tuple:
    results = YoutubeSearch(query, max_results=1).to_dict()[0]

    title = results['title'][:40]
    thumbnail = results['thumbnails'][0]
    thumb_name = f'{title}.jpg'

    headers = {'User-Agent': UserAgent().random}

    async with ClientSession(headers=headers) as session:
        async with session.get(thumbnail, allow_redirects=True) as response:
            thumb = await response.read()

    async with open(thumb_name, 'wb') as f:
        await f.write(thumb)

    return thumb, results, title


async def download_video(results: dict) -> str:
    link = f"https://youtube.com{results['url_suffix']}"
    duration = results['duration']

    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        ydl.cache.remove()

        info_dict = ydl.extract_info(link, download=False)
        audio_file = ydl.prepare_filename(info_dict)
        ydl.process_info(info_dict)

    secmul, dur, dur_arr = 1, 0, duration.split(':')

    for i in dur_arr[::-1]:
        dur += int(float(i)) * secmul
        secmul *= 60

    return audio_file, dur


@Client.on_message(
    command(
        commands=['music'],
        prefixes=['.', '/']
    ) & (me | private)
)
async def music(_: Client, message: Message):
    query = ' '.join(message.command[1:])
    msg = await message.reply(FINDING_SONG)

    try:
        thumb, results, title = await search_video(query)
        thumb_name = f'{title}.jpg'
    except Exception as ex:
        await msg.edit(SONG_NOT_FOUND)
        raise ex

    await msg.edit(DOWNLOADING_FILE)

    try:
        audio_file, duration = await download_video(results)

        await msg.edit(UPLOADING_FILE)

        await message.reply_audio(
            audio_file,
            caption=CAPTION,
            thumb=thumb_name,
            title=title,
            duration=duration,
        )

        await msg.delete()
    except Exception as ex:
        await msg.edit(ERROR)
        raise ex

    finally:
        if await path.isfile(thumb_name):
            await remove(thumb_name)
            print(thumb_name)
        if await path.isfile(audio_file):
            await remove(audio_file)
            print(audio_file)
