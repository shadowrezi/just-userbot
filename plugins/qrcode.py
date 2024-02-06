from pyrogram import Client
from pyrogram.filters import command, me, private
from pyrogram.types import Message

from aiofiles.os import remove, listdir
import qrcode
import cv2



@Client.on_message(
    command(
        commands=['qrcode'],
        prefixes=['.', '/']
    ) & (me | private)
)
async def create_qrcode(_: Client, message: Message):
    data = ' '.join(message.command[1:])
    filename = 'temp2.png'
    
    try:
        qrcode\
            .make(data=data)\
            .save(filename)
    
        await message.reply_photo(
            photo=filename,
            quote=True
        )
    
    finally:
        await remove(filename)
    

@Client.on_message(
    command(
        commands=['decode'],
        prefixes=['.', '/']
    ) & (me | private)
)
async def decoder(client: Client, message: Message):
    msg = message.reply_to_message
    
    if not msg:
        await client.download_media(message, 'temp.png')
    
    if not hasattr(message, 'photo'):
        return 

    if not (msg.photo or message.photo):
        await message.reply('**Replied message must be a photo-message**', quote=True)
        return
    
    await client.download_media(msg, 'temp.png')
    
    try:
        img = cv2.imread('downloads/temp.png')

        det = cv2.QRCodeDetector()
        tx, _, _ = det.detectAndDecode(img)

        await message.edit("**Decoded Text:** " + f'<code>{tx}</code>')
    
    finally:
        if 'downloads' in await listdir():
            return
        if 'temp.png' in await listdir('downloads'):
            await remove('downloads/temp.png')

