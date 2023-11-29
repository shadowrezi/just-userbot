from asyncio import sleep
from typing import Literal

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

from misc.filters import startswith


is_typing = True
is_bold = True


async def toggle_state(state_var_name: Literal['is_typing', 'is_bold'], message: Message, text: str):
    global is_typing, is_bold

    if state_var_name == 'is_typing':
        is_typing = not is_typing
        state_var = is_typing
    elif state_var_name == 'is_bold':
        is_bold = not is_bold
        state_var = is_bold
    else:
        raise ValueError("Invalid state variable name")
    
    state = 'enabled' if state_var else 'disabled'
    await message.reply(f'<b>{text} is {state}! </b>')


@Client.on_message(
    filters.command(
        commands='switch-typing',
        prefixes=['.', '/']
    ) & filters.me
)
async def switch_typing(_, message: Message):
    await toggle_state('is_typing', message, 'Typing')


@Client.on_message(
    filters.command(
        commands=['switch-bold'],
        prefixes=['.', '/']
    ) & filters.me
)
async def switch_bold(_, message: Message):
    await toggle_state('is_bold', message, 'Bold')


@Client.on_message(startswith('/') & filters.me)
async def type(_, message: Message):
    global is_typing
    global is_bold

    if not is_typing:
        return

    z = ''
    if is_bold:
        z = '**'

    if message.voice is not None:
        return

    original_text = message.text[1:]  # without `/` symbol
    text = message.text[1:]
    tbp = ""  # to be printed
    typing_symbol = "▒"  # symbol that will be writed after your letters

    while tbp != original_text:
        try:
            await message.edit(
                z + tbp + typing_symbol + z  # `**` for bold text
            )
            await sleep(0.05)  # delay beetween symbol editing (25 ms)

            tbp = tbp + text[0]
            text = text[1:]

            await message.edit(
                z + tbp + z  # `**` for bold text
            )
            await sleep(0.05)  # delay beetween symbol editing (25 ms)

        except FloodWait as fd:  # if messages are too often edited
            await sleep(fd.value)
