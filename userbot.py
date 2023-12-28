from os import getenv, rmdir
from os.path import exists

import signal
import sys

from pyrogram import Client
import uvloop

from dotenv import load_dotenv


load_dotenv()

API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')

uvloop.install()
app = Client(
    'my_account',
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
    signal.signal(
        signal.SIGTSTP,
        handle_ctrl_z
    )
    print('Starting bot...')

    app.run()
    if __name__ != '__main__':
        return
    with app:
        message.delete()


def handle_ctrl_z(signal, frame):
    print('Exiting bot...')

    if exists('downloads'):
        rmdir('downloads')

    sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    finally:
        if exists('downloads'):
            rmdir('downloads')
