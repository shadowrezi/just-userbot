from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait


async def edit_with_retry(message: Message, text: str, time: int | float = 0.5):
    try:
        await message.edit(text)
        await sleep(time)
    except FloodWait as fw:
        await sleep(fw.value)


@Client.on_message(
    filters.command(
        commands=["heart"],
        prefixes=['.', '/']
    ) & filters.me
)
async def mini_magic(_, message: Message):
    text_parsing = ' '.join(message.command[1:])

    if text_parsing:
        text = f'**{text_parsing}**'
    else:
        text = '❤️'

    base_frame = """
✨💎💎✨💎💎✨
💎💎💎💎💎💎💎
💎💎💎💎💎💎💎
✨💎💎💎💎💎✨
✨✨💎💎💎✨✨
✨✨✨💎✨✨✨
""".strip()

    frames = [
        base_frame,
        base_frame.replace("💎", "🌺"),
        base_frame.replace("💎", "😘").replace("✨", "☁️"),
        base_frame.replace("💎", "🌸"),
        base_frame.replace("💎", "🐸").replace("✨", "🌾"),
        base_frame.replace("💎", "💥").replace("✨", "🔫"),
        base_frame.replace("💎", "💟").replace("✨", "☁️"),
        base_frame.replace("💎", "💖").replace("✨", "🍀"),
        base_frame.replace("💎", "🐼").replace("✨", "🌴"),
    ]
    
    for frame in frames:
        await edit_with_retry(message, frame)

    await edit_with_retry(message, text)
