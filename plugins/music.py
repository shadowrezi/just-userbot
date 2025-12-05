from aiohttp import ClientSession
from pyrogram import Client
from pyrogram.filters import me, private, command
from pyrogram.types import Message

from aiofiles import open
from aiofiles.os import remove, path

import yt_dlp
from fake_useragent import UserAgent


# CONFIG
OWNER = 'ShadowRezi'
CAPTION = f'<b>🎧 Uploader @{OWNER}</b>'
FINDING_SONG = '<b>🔎 Finding song...</b>'
SONG_NOT_FOUND = f"<b>❌ Song not found.\nPlease give a valid song name.\nIf bot doesn't work, write @{OWNER}</b>"
DOWNLOADING_FILE = '<b>📥 Downloading file...</b>'
UPLOADING_FILE = '<b>📤 Uploading file...</b>'
ERROR = '❌ Error occurred'

YDL_OPTIONS = {
    'format': 'bestaudio[ext=m4a]',
    'quiet': True
}


# 🔎 SEARCH YOUTUBE VIDEO
async def search_video(query: str):
    opts = {
        "quiet": True,
        "extract_flat": True,
    }

    with yt_dlp.YoutubeDL(opts) as ydl:
        data = ydl.extract_info(f"ytsearch10:{query}", download=False)

    if not data or "entries" not in data:
        return None

    for e in data["entries"]:
        url = e.get("url", "")

        if not url:
            continue

        if "/shorts/" in url:
            continue
        if "/watch" not in url:
            continue

        return {
            "id": e["id"],
            "title": e.get("title", "Unknown"),
            "duration": e.get("duration"),
            "thumbnail": e.get("thumbnails", [{}])[0].get("url"),
            "url": f"https://www.youtube.com/watch?v={e['id']}",
        }

    return None


# 📥 DOWNLOAD AUDIO + THUMBNAIL
async def download_video(results: dict):
    link = results["url"]
    title = results["title"][:40]
    duration = results["duration"]
    thumbnail = results["thumbnail"]

    safe_title = title.replace("/", "")
    thumb_name = f"{safe_title}.jpg"

    headers = {"User-Agent": UserAgent().random}

    # download thumbnail
    async with ClientSession(headers=headers) as session:
        async with session.get(thumbnail) as resp:
            image = await resp.read()

    async with open(thumb_name, "wb") as f:
        await f.write(image)

    # download audio
    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        ydl.cache.remove()
        info = ydl.extract_info(link, download=False)
        audio_file = ydl.prepare_filename(info)
        ydl.process_info(info)

    # duration → seconds
    dur = 0
    mult = 1
    if duration:
        dur = int(duration)
        
        #for part in duration.split(":")[::-1]:
        #    dur += int(part) * mult
        #    mult *= 60

    return audio_file, dur, title, thumb_name


# 🎵 PYROGRAM HANDLER
@Client.on_message(
    command(['music'], prefixes=['.', '/']) & (me | private)
)
async def music(_: Client, message: Message):
    query = ' '.join(message.command[1:])
    msg = await message.reply(FINDING_SONG)

    try:
        results = await search_video(query)
        if not results:
            return await msg.edit(SONG_NOT_FOUND)
    except Exception as ex:
        await msg.edit(SONG_NOT_FOUND)
        raise ex

    await msg.edit(DOWNLOADING_FILE)

    try:
        audio_file, duration, title, thumb_name = await download_video(results)

        await msg.edit(UPLOADING_FILE)

        await message.reply_audio(
            audio_file,
            caption=CAPTION,
            thumb=thumb_name,
            title=title,
            duration=duration,
            performer="ShadowRezi"
        )

        await msg.delete()

    except Exception:
        await msg.edit(ERROR)
        raise

    # cleanup files
    if await path.isfile(thumb_name):
        await remove(thumb_name)

    if 'audio_file' in locals() and await path.isfile(audio_file):
        await remove(audio_file)
