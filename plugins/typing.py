from asyncio import sleep
from typing import Literal

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

from misc.filters import startswith
from misc.utils import Flag


is_typing = Flag()
is_bold = Flag()


@Client.on_message(
    filters.command(
        commands='switch-typing',
        prefixes=['.', '/']
    ) & filters.me
)
async def switch_typing(_, message: Message):
    is_typing.toggle()
    await message.reply('Typing was toggled!')


@Client.on_message(
    filters.command(
        commands=['switch-bold'],
        prefixes=['.', '/']
    ) & filters.me
)
async def switch_bold(_, message: Message):
    is_bold.toggle()
    await message.reply('Bold was toggled!')


@Client.on_message(startswith('/') & filters.me)
async def type(_, message: Message):
    if not is_typing.status:
        return

    z = ''
    if is_bold.status:
        z = '**'

    if message.voice is not None:
        return

    original_text = message.text[1:]
    text = message.text[1:]
    tbp = ""
    typing_symbol = "▒"

    while tbp != original_text:
        try:
            await message.edit(
                z + tbp + typing_symbol + z
            )
            await sleep(0.05)

            tbp = tbp + text[0]
            text = text[1:]

            await message.edit(
                z + tbp + z
            )
            await sleep(0.05)

        except FloodWait as fd:
            await sleep(fd.value)
