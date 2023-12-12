from pathlib import Path

from asyncio import gather, create_task
from aiofiles import open

from pyrogram import Client, filters
from pyrogram.types import Message


async def readlines(filename: str) -> list:
    async with open(filename) as f:
        return await f.readlines()


@Client.on_message(
    filters.command(
        commands=['count'],
        prefixes=['.', '/']
    ) & filters.me
)
async def count(_, message: Message):
    all_files = [
        str(file)
        for file in Path('.').rglob('*.py')
        if 'venv' not in str(file) and \
        '__pycache__' not in str(file) and \
        'test.py' not in str(file)
    ]

    list_lines = [create_task(readlines(file)) for file in all_files]

    await gather(*list_lines)

    lines = [item for sublist in list_lines for item in sublist.result()]

    count_lines = len(lines)  # length of list of lines

    count_symbols = len(''.join(lines))  # length of every line in list of lines

    await message.reply(
        '**This project is writed by '
        f'{count_lines} lines of code and by {count_symbols} symbols! **'
        '\n\n'
        '@ShadowRazea\n'
        '<a href=https://github.com/shadowrezi/just-userbot>GitHub repo</a>'
    )


