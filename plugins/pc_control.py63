from os import system
from platform import system as get_os

from pyrogram import filters, Client
from pyrogram.types import Message


OS = get_os()  # your operational system (Windows, Linux, MacOS)


async def run(linux_command: str, windows_command: str, os: str):
    if os == 'Linux':
        system(linux_command)
    elif os == 'Windows':
        system(windows_command)
    else:
        raise ValueError('Unsupported Operational System')


@Client.on_message(
    filters.command(
        commands=['shutdown'],
        prefixes=['.', '/']
    ) & filters.me
)
async def shutdown(_, message: Message):
    run('shutdown', 'shutdown -f -t 60', OS)

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
    run('shutdown -r', 'shutdown -r -t 60', OS)

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
    run('shutdown -c', 'shutdown -a', OS)

    await message.reply(
        '<code>Plan for exclusion canceled</code>',
        quote=True
    )
