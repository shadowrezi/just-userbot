from time import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import enums


typing_enabled = True


@Client.on_message(filters.command('switch-typing', '.') & filters.me)
async def switch_typing(_, message: Message):
    global typing_enabled

    typing_enabled = not typing_enabled
    
    state = 'enabled' if typing_enabled else 'disabled'
    
    await message.reply(
        f'<b>Typing is {state}! </b>'
    )


@Client.on_message(filters.me)
async def type(_, msg: Message):
    global typing_enabled

    if not typing_enabled:
        return
    
    if msg.voice is not None:
        return
    
    original_text = msg.text
    text = msg.text
    tbp = ""  # to be printed
    typing_symbol = "▒"  # symbol that will after your letters

    while tbp != original_text:
        try:
            await msg.edit(
                '**' + tbp + typing_symbol + '**',  # `**` for bold text
                parse_mode=enums.ParseMode.MARKDOWN
            )
            sleep(0.05)  # delay beetween symbol editing (50 ms)

            tbp = tbp + text[0]
            text = text[1:]

            await msg.edit(
                '**' + tbp + '**',  # `**` for bold text
                parse_mode=enums.ParseMode.MARKDOWN
            )
            sleep(0.05)  # delay beetween symbol editing (50 ms)

        except FloodWait as e:  # if messages are too often edited
            sleep(e.x)
