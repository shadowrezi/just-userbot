from pyrogram import Client
from pyrogram.filters import me, command
from pyrogram.types import Message

from misc.filters import in_
from misc.utils import Flag

is_parsemode = Flag(True)


@Client.on_edited_message(
    in_('<') &
    in_('>') &
    me
)
@Client.on_message(
    in_('<') &
    in_('>') &
    me
)
async def update_parsemode(_: Client, message: Message):
    if is_parsemode.status:
        await message.edit(message.text)


@Client.on_message(
    command(
        commands=['switch-parsemode'],
        prefixes=['.', '/']
    ) & me
)
async def switch_parsemode(_: Client, message: Message):
    is_parsemode.toggle()
