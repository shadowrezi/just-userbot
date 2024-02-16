from functools import singledispatch

from pyrogram import filters
from pyrogram.types import Message

@singledispatch
def in_message(text):
    pass

@in_message.register
def _(text: str):
    async def filter(flt, _, message: Message):
        if message.text is None:
            return False
        return flt.text in message.text
    return filters.create(filter, text=text)  # text=text, we get it by `flt`

@in_message.register
def in_message(text: list):
    async def filter(flt, _, message: Message):
        if message.text is None:
            return False
        
        for i in flt.text:
            if i in message.text:
                return False
        return True
    return filters.create(filter, text=text)


def startswith(target: str):
    async def filter(flt, _, message: Message):
        if message.text is None:
            return False
        return message.text.startswith(flt.target)
    return filters.create(filter, target=target)

