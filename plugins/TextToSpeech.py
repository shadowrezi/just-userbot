import os

from pyrogram import Client, filters
from pyrogram.types import Message

from gtts import gTTS


@Client.on_message(
    filters.command(
        commands=['gtts'],
        prefixes=['.', '/']
    )
)
async def text_to_speech(_, message: Message):
    data = ' '.join(message.command[1:])
    filename = 'downloads/temp.mp3'

    # await message.edit(f'**{data}**')
    
    try:
        gTTS(
            text=data,
            lang='ru'
        ).save(filename)
    
        await message.reply_voice(
            voice=filename,
            quote=True,
            caption='Voiced by gTTS\n@ShadowRazea'
        )
    finally:
        os.remove(filename)
