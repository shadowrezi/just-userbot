from os import system
from platform import system as get_os

from pyrogram import filters, Client
from pyrogram.types import Message


OS = get_os()  # your operational system (Windows, Linux, MacOS)


@Client.on_message(
    filters.command(
        commands=['shutdown'],
        prefixes=['.', '/']
    ) & filters.me
)
async def shutdown(_, message: Message):
    if OS == 'Linux':
        system('shutdown')
    elif OS == 'Windows':
        system('shutdown -f -t 60')  # -t <time in secs>
    
    await message.reply(
        '<code>Computer will be turned off in 1 minute</code>',
        quote=True
    )


@Client.on_message(
    filters.command(
        commands=['restart'],
        prefixes=['.', '/']
    ) & filters.me
)
async def restart(_, message: Message):
    if OS == 'Linux':
        system('shutdown -r')
    elif OS == 'Windows':
        system('shutdown -r -t 60')

    await message.reply(
        '<code>Computer will be restarted in 1 minute</code>',
        quote=True
    )


@Client.on_message(
    filters.command(
        commands=['cancel'],
        prefixes=['.', '/']
    ) & filters.me
)
async def cancel(_, message: Message):
    if OS == 'Linux':
        system('shutdown -c')
    elif OS == 'Windows':
        system('shutdown -a')

    await message.reply(
        '<code>Plan for exclusion canceled</code>',
        quote=True
    )
