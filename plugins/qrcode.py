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

    main_message = msg if msg else message

    if not hasattr(main_message, 'photo'):
        return
    
    if not (main_message.photo):
        await message.reply('**Message must be a photo-message**', quote=True)
        return
        
    
    await client.download_media(main_message, 'temp.png')
    
    try:
        img = cv2.imread('downloads/temp.png')
        tx, _, _ = cv2.QRCodeDetector().detectAndDecode(img)

        await message.edit("**Decoded Text:** " + f'<code>{tx}</code>')
    
    finally:
        if 'downloads' in await listdir():
            return
        if 'temp.png' in await listdir('downloads'):
            await remove('downloads/temp.png')


