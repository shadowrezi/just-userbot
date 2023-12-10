from os import listdir

from pyrogram import Client, filters
from pyrogram.types import Message


def get_py_files_in_dir(dir: str) -> list[str]:
    return [
        dir + '/' + file
        for file in listdir(f'./{dir}')
        if file.endswith('.py')
    ]


@Client.on_message(
    filters.command(
        commands=['count'],
        prefixes=['.', '/']
    ) & filters.me
)
async def count(_, message: Message):
    plugins = get_py_files_in_dir('plugins')
    miscs = get_py_files_in_dir('misc')

    all_files = ['userbot.py'] + plugins + miscs
 
    list_lines = (
        [open(file).readlines() for file in all_files]
    )
    
    lines = [item for sublist in list_lines for item in sublist]

    count_lines = len(lines)

    count_symbols = len(''.join(lines))

    await message.reply(
        '**This project is writed by '
        f'{count_lines} lines of code and by {count_symbols} symbols! **'
        '\n\n'
        '@ShadowRazea\n'
        '<a href=https://github.com/shadowrezi/just-userbot>GitHub repo</a>'
    )

