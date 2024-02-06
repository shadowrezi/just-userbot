from pyrogram import Client
from pyrogram.filters import command, me, private
from pyrogram.types import Message

from aiofiles.os import remove, listdir

from gtts import gTTS


@Client.on_message(
    command(
        commands=['gtts'],
        prefixes=['.', '/']
    ) & (me | private)
)
async def text_to_speech(_: Client, message: Message):
    data = ' '.join(message.command[1:])
    filename = 'downloads/temp.mp3'
    
    try:
        gTTS(
            text=data,
            lang='uk'
        ).save(filename)
    
        await message.reply_voice(
            voice=filename,
            quote=True,
            caption='Voiced by gTTS'
        )
    finally:
        if 'downloads' not in await listdir():
            return
        if filename in await listdir('downloads'):
            await remove(filename)
