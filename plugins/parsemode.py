from pyrogram import Client, filters
from pyrogram.types import Message

from filters import in_message


@Client.on_message(
    in_message('<') &
    in_message('>') &
    filters.me
)
async def update_parsemode(_: Client, message: Message):
    '''
    Update message with html & markdown parsemodes
    '''
    await message.edit(message.text)
