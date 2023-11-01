from pyrogram import filters
from pyrogram.types import Message


def in_message(text):
    async def filter(flt, _, message: Message):
        if message.text is None:
            return False
        return flt.text in message.text
    return filters.create(filter, text=text)  # text=text, we get it by `flt`
