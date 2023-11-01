from os import listdir

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(
        commands=['count'],
        prefixes=['.', '/']
    ) & filters.me
)
async def count(_, message: Message):
    plugins = [
        'plugins/' + file
        for file in listdir('./plugins')
    ]
    
    all_files = listdir('.') + plugins
 
    all_py_files = (file for file in all_files if file.endswith('.py'))
    
    lines = sum(
        [
            len(open(i, 'r').readlines())
            for i in all_py_files
        ]
    )
    await message.reply(
        f'**This project is writed by {lines} lines of code! **'
        '\n\n'
        '@ShadowRazea\n'
        '<a href=https://github.com/shadowrezi/just-userbot>GitHub repo</a>'
    )
