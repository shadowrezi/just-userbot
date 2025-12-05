from os import getenv, environ
import asyncio
from shutil import rmtree

from aiofiles.os import path

import sys

from pyrogram import Client
import uvloop

from colorama import Fore

from dotenv import load_dotenv


load_dotenv()

environ["PYROGRAM_DISABLE_UVLOOP"] = "1"

API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')

# uvloop.install()
app = Client(
    'telegram',
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={
        'root': 'plugins'
    }
)

if __name__ == '__main__':
    with app:
        message = app.send_message('me', '</b>Bot was started!</b>')
        message.pin(True)


def main():
    # signal.signal(
    # signal.SIGTSTP,
    # await handle_ctrl_z
    # )
    print(Fore.LIGHTGREEN_EX + 'Starting bot...' + Fore.RESET)

    app.run()
    if __name__ != '__main__':
        return
    with app:
        message.unpin()
        message.delete()


async def handle_ctrl_z(signal, frame):
    print(Fore.LIGHTRED_EX + 'Exiting bot...' + Fore.RESET)

    if await path.exists('downloads'):
        rmtree('downloads')

    sys.exit(0)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    finally:
        if asyncio.run(path.exists('downloads')):
            rmtree('downloads')
