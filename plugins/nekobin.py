from pyrogram import Client, filters
from pyrogram.types import Message

from nekobin import Nekobin


@Client.on_message(
    filters.command(
        'bin', ['.', '/']
    ) & filters.me
)
async def bin(_, message: Message):
    nb = Nekobin()

    text = message.reply_to_message.text if message.reply_to_message else message.text[4:]

    result = await nb.paste(text)

    if result.ok:
        await message.reply(
            f'Your bin {result.url}',
            quote=True,
            disable_web_page_preview=True
        )
    else:
        await message.reply(f'Error: {result.message}')
