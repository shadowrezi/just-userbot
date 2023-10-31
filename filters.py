from pyrogram import filters
from pyrogram.types import Message


def in_message(text):
    async def filter(flt, _, message: Message):
        return flt.text in message.text
    return filters.create(filter, text=text)
