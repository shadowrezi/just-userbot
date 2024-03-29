from asyncio import sleep

from pyrogram import Client
from pyrogram.filters import me, private, voice, video_note, dice, command
from pyrogram.types import Message

from misc.utils import Flag


is_voice_message_allowed = Flag()


@Client.on_message(
    command(
        commands=['switch-voice'],
        prefixes=['.', '/']
    ) & me
)
async def switch_voice(_: Client, message: Message) -> None:
    is_voice_message_allowed.toggle()


@Client.on_message(private & (voice | video_note))
async def save_and_delete_voice_message(client: Client, message: Message) -> None:
    if is_voice_message_allowed.status:
        return
    voice = await message.forward('me')
    
    user = message.from_user
    text = f'''
    <a href="https://t.me/{user.username}">
        {user.first_name}
    </a>
    '''.strip()

    await voice.reply(text, quote=True)
    await message.reply('This user forbids the use of voice message :)')
    await message.delete()

