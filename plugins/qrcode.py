import os

import qrcode
import cv2

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(
        commands=['qrcode'],
        prefixes=['.', '/']
    ) & filters.me
)
async def create_qrcode(_, message: Message):
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
        os.remove(filename)
    

@Client.on_message(
    filters.command(
        commands=['decode'],
        prefixes=['.', '/']
    ) & filters.me
)
async def decoder(client: Client, message: Message):
    msg = message.reply_to_message
    
    if not msg:
        await message.reply('**Reply this command to photo-message!**', quote=True)
        return
    
    photo = msg.photo
    
    if not photo:
        await message.reply('**Replied message must be a photo-message**', quote=True)
        return
    
    await client.download_media(msg, 'temp.png')
    
    try:
        img = cv2.imread('downloads/temp.png')

        det = cv2.QRCodeDetector()
        tx, _, _ = det.detectAndDecode(img)

        await message.edit("**Decoded Text:** " + f'<code>{tx}</code>')
    
    finally:
        os.remove('downloads/temp.png')
