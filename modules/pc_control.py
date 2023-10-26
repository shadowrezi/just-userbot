from os import system

from pyrogram import filters, Client


@Client.on_message(filters.me & filters.command('shutdown', '.'))
async def shutdown(_, msg):
    system('shutdown')

    await msg.reply(
        '<code>Computer will be turned off in 1 minute</code>',
        quote=True
    )


@Client.on_message(filters.me & filters.command('cancel', '.'))
async def cancel_shutdown(_, msg):
    system('shutdown -c')

    print('<code>Shutting down was canceled!</code>')

    await msg.reply(
        '<code>Plan for exclusion canceled</code>',
        quote=True
    )


@Client.on_message(filters.me & filters.command('restart', '.'))
async def restart(_, msg):
    system('shutdown -r')

    await msg.reply(
        '<code>Computer will be restarted in 1 minute</code>',
        quote=True
    )
