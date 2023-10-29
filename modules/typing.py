from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import enums


typing_enabled = True


@Client.on_message(
    filters.command(
        commands='switch-typing',
        prefixes=['.', '/']
    ) & filters.me
)
async def switch_typing(_, message: Message):
    global typing_enabled

    typing_enabled = not typing_enabled
    
    state = 'enabled' if typing_enabled else 'disabled'
    
    await message.reply(
        f'<b>Typing is {state}! </b>'
    )


@Client.on_message(filters.me)
async def type(_, message: Message):
    global typing_enabled

    if not typing_enabled:
        return
    
    if message.voice is not None:
        return
    
    original_text = message.text
    text = message.text
    tbp = ""  # to be printed
    typing_symbol = "▒"  # symbol that will be writed after your letters

    while tbp != original_text:
        try:
            await message.edit(
                '**' + tbp + typing_symbol + '**',  # `**` for bold text
                parse_mode=enums.ParseMode.MARKDOWN
            )
            await sleep(0.05)  # delay beetween symbol editing (50 ms)

            tbp = tbp + text[0]
            text = text[1:]

            await message.edit(
                '**' + tbp + '**',  # `**` for bold text
                parse_mode=enums.ParseMode.MARKDOWN
            )
            await sleep(0.05)  # delay beetween symbol editing (50 ms)

        except FloodWait as e:  # if messages are too often edited
            sleep(e.x)
