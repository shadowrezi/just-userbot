from pyrogram import Client, filters
from pyrogram.types import Message

from misc.filters import in_message

'''
@Client.on_edited_message(
    in_message('<') &
    in_message('>') &
    filters.me
)
async def update_edited_parsemode(_: Client, message: Message):
    await message.edit(message.text)
'''
@Client.on_edited_message(
    in_message('<') &
    in_message('>') &
    filters.me
)
@Client.on_message(
    in_message('<') &
    in_message('>') &
    filters.me
)
async def update_parsemode(_: Client, message: Message):
    await message.edit(message.text)
