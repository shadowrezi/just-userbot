from os import listdir

import re

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(
        commands=['commands'],
        prefixes=['.', '/']
    ) & filters.me
)
async def all_commands(_, message: Message):
    files = listdir("plugins/")
    py_files = [
        file 
        for file in files
        if file.endswith('.py')
    ]

    text = ''

    for i in py_files:
        with open(f'plugins/{i}', 'r') as f:
            text += f.read()

    pattern = re.compile(r'commands=\[[^]]*]')
    
    commands = ''
    for command in pattern.findall(text):
        commands += command[11:-2] 
        commands += '\n'

    await message.reply(commands)
