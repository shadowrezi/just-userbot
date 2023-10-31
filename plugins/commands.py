from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(
        commands=['commands'],
        prefixes=['.', '/']
    ) & filters.me
)
async def all_commands(_, message: Message):
    HANDLERS = [
        'gpt',
        'music',
        'shutdown',
        'restart',
        'cancel',
        'switch-typing',
        'magic',
        'commands',
        'qrcode',
        'decode'
    ]
    PREFIX = '.'

    commands = [
        f'<code>{PREFIX}{handle}</code>'
        for handle in HANDLERS
    ]

    await message.reply(
        '**Prefixes:\n/\n.\n\nList of all commands:\n **' + '\n'.join(commands)
    )
