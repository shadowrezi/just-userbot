from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait


@Client.on_message(
    filters.command(
        commands=["magic"],
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

    frame_2 = base_frame.replace("💎", "🌺")
    frame_3 = base_frame.replace("💎", "😘").replace("✨", "☁️")
    frame_4 = base_frame.replace("💎", "🌸")
    frame_5 = base_frame.replace("💎", "🐸").replace("✨", "🌾")
    frame_6 = base_frame.replace("💎", "💥").replace("✨", "🔫")
    frame_7 = base_frame.replace("💎", "💟").replace("✨", "☁️")
    frame_8 = base_frame.replace("💎", "💖").replace("✨", "🍀")
    frame_9 = base_frame.replace("💎", "🐼").replace("✨", "🌴")

    frames = [base_frame, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9]

    async def edit_with_retry(message: Message, text: str, time: int | float = 0.5):
        try:
            await message.edit(text)
            await sleep(time)
        except FloodWait as fw:
            await sleep(fw.value)

    for frame in frames:
        await edit_with_retry(message, frame)

    await edit_with_retry(message, text)
