from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from re import search as re_search
from asyncio import sleep
from random import choice


# ❤️ magic text=str;
@Client.on_message(filters.command(
    commands="magic", prefixes='.') & filters.me
)
async def magic(client, msg: Message):

    # Парсинг текста
    text_parsing = re_search(r'(?<=text\\=).+?(?=;)', msg.text)

    # Обработка парсинга текста
    if text_parsing:
        text = text_parsing[0]
    # Value by default
    else:
        text = '❤️'

    # Фреймы
    frame_1 = """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍"""

    frame_2 = frame_1.replace("❤️", "🧡")

    frame_3 = frame_1.replace("❤️", "💛")

    frame_4 = frame_1.replace("❤️", "💚")

    frame_5 = frame_1.replace("❤️", "💙")

    frame_6 = frame_1.replace("❤️", "💜")

    frame_7 = frame_1.replace("❤️", "🖤")

    frame_8 = frame_1.replace("❤️", "🤎")

    # Ассортимент сердец
    heart_assortment = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤎"]

    # Рандомные фреймы
    frame_9 = "".join(
        list(map(lambda x: "\\n" if x == "\\n" else choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

    frame_10 = "".join(
        list(map(lambda x: "\\n" if x == "\\n" else choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

    frame_11 = "".join(
        list(map(lambda x: "\\n" if x == "\\n" else choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

    frame_12 = "".join(
        list(map(lambda x: "\\n" if x == "\\n" else choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

    frame_13 = "".join(
        list(map(lambda x: "\\n" if x == "\\n" else choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

    # Объединяем все фреймы в список
    frames_to_print = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9, frame_10,
                       frame_11, frame_12, frame_13, frame_1]

    # Отображаем все фреймы
    for frame in frames_to_print:

        try:
            await msg.edit(frame)
            await sleep(.4)

        except FloodWait as fw:
            await sleep(fw.value)


# ❤️ mini-magic text=str;
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

    # Объединяем все фреймы в список
    frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9]

    # Отображаем каждый фрейм
    for frame in frames:

        try:
            await msg.edit(frame)
            await sleep(.5)

        except FloodWait as fw:
            await sleep(fw.value)

    # Отбражаем конечное сообщение
    try:
        await msg.edit(text)
        await sleep(0.5)

    except FloodWait as fw:
        await sleep(fw.value)
