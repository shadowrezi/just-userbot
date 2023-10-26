from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram import enums


@Client.on_message(filters.me)
async def type(_, msg):
    if msg.voice is not None:
        print(0)
        return
    print(1)
    text_ = msg.text
    text = msg.text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while(tbp != text_):
        try:
            await msg.edit(
                '**' + tbp + typing_symbol + '**',
                parse_mode=enums.ParseMode.MARKDOWN
            )
            sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            await msg.edit(
                '**' + tbp + '**',
                parse_mode=enums.ParseMode.MARKDOWN    
            )
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)
