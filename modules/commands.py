from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command('commands', prefixes='.'))
async def all_commands(_, message: Message):
    HANDLERS = ['gpt', 'music', 'shutdown', 'restart', 'cancel', 'switch-typing', 'magic', 'commands']
    PREFIX = '.'

    print(1)

    await message.reply(
        '**List of all commands:\n **'
         + '\n'.join(f'<code>{PREFIX}{handle}</code>' for handle in HANDLERS)
    )
