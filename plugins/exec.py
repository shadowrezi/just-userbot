from pyrogram import filters, Client
from pyrogram.types import Message


@Client.on_message(filters.command('py', ':'))
async def executing(_, message):
    code = ' '.join(message.command[1:])
    
    code_return = exec(code)
    if code_return:
        await message.reply(code_return)
