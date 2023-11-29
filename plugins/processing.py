from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait


@Client.on_message(
    filters.command(
        commands=['processing'],
        prefixes=['.', '/']
    ) & filters.me
)
async def processing(_, message: Message):
    ''' .processing <time> <text> '''
    time = int(message.command[1])
    text = ' '.join(message.command[2:])

    filled_symbol = '='
    progress_length = 10  # The length of the progress bar

    for i in range(1, 101, 2):
        try:
            filled_chars = filled_symbol * (i * progress_length // 100)
            empty_chars = ' ' * (progress_length - len(filled_chars))
            progress_text = f"[{filled_chars}{empty_chars}] {i}%"

            await message.edit(f'Percent <code>{progress_text}</code>')
        except FloodWait as fd:
            await sleep(int(fd.value))
        await sleep(time / 100)

    await message.edit('**' + text + '**')
