from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

from re import search as re_search


@Client.on_message(filters.command(commands="mini-magic", prefixes='.') & filters.me)
async def mini_magic(client, msg: Message):

    # Парсинг текста
    text_parsing = re_search(r'(?<=text\\=).+?(?=;)', msg.text)

    # Обработка парсинга текста
    if text_parsing:
        text = text_parsing[0]
    # Value by default
    else:
        text = '❤️'

    # Фреймы
    frame_1 = """✨💎💎✨💎💎✨
💎💎💎💎💎💎💎
💎💎💎💎💎💎💎
✨💎💎💎💎💎✨
✨✨💎💎💎✨✨
✨✨✨💎✨✨✨
"""

    frame_2 = frame_1.replace("💎", "🌺")
    frame_3 = frame_1.replace("💎", "😘").replace("✨", "☁️")
    frame_4 = frame_1.replace("💎", "🌸")
    frame_5 = frame_1.replace("💎", "🐸").replace("✨", "🌾")
    frame_6 = frame_1.replace("💎", "💥").replace("✨", "🔫")
    frame_7 = frame_1.replace("💎", "💟").replace("✨", "☁️")
    frame_8 = frame_1.replace("💎", "💖").replace("✨", "🍀")
    frame_9 = frame_1.replace("💎", "🐼").replace("✨", "🌴")

    frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9]

    for frame in frames:

        try:
            await msg.edit(frame)
            await sleep(.5)

        except FloodWait as fw:
            await sleep(fw.value)

    try:
        await msg.edit(text)
        await sleep(0.5)

    except FloodWait as fw:
        await sleep(fw.value)
