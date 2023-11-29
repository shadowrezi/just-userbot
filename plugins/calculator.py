from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command('', ['~']) & filters.me)
async def calculator(_, message: Message):
    print(message.command[1:])
    await message.reply(eval(message.text[2:]), quote=True)

