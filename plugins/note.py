from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(
        commands=['note'],
        prefixes=['.', '/']
    ) & filters. me
)
async def note(_, message: Message):
    msg = message.reply_to_message
    
    if not msg:  # if main message isn't replied to message
        await message.delete()
        return
    
    await msg.forward('self')  # forward replied message to `Saved notes`
    await message.delete()
