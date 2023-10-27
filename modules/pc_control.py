from os import system
from platform import system as get_os

from pyrogram import filters, Client


OS = get_os()  # your operational system (Windows, Linux, MacOS)


@Client.on_message(filters.me & filters.command('shutdown', '.'))
async def shutdown(_, msg):
    if OS == 'Linux':
        system('shutdown')
    elif OS == 'Windows':
        system('shutdown -f -t 60')  # -t <time in secs>
    
    await msg.reply(
        '<code>Computer will be turned off in 1 minute</code>',
        quote=True
    )


@Client.on_message(filters.me & filters.command('restart', '.'))
async def restart(_, msg):
    if OS == 'Linux':
        system('shutdown -r')
    elif OS == 'Windows':
        system('shutdown -r -t 60')

    await msg.reply(
        '<code>Computer will be restarted in 1 minute</code>',
        quote=True
    )


@Client.on_message(filters.me & filters.command('cancel', '.'))
async def cancel_shutdown(_, msg):
    if OS == 'Linux':
        system('shutdown -c')
    elif OS == 'Windows':
        system('shutdown -a')

    await msg.reply(
        '<code>Plan for exclusion canceled</code>',
        quote=True
    )
