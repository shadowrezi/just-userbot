from os import getenv, system
from sqlite3 import OperationalError
from platform import system as get_os

import signal
import sys

from rich import console

from pyrogram import Client
import uvloop  # for speeding up pyrogram

from dotenv import load_dotenv


'''
write in file `.env` your api id and hash, for example:

API_ID=123
API_HASH=321

OPENAI_TOKEN=s1asdasdasdjqojdasjoiqioifewninweionfweio

it's all needed data

WITHOUT WHITESPACE beetween name and value
'''

load_dotenv()

API_ID = getenv('API_ID')  # get on the telegram's official site
API_HASH = getenv('API_HASH')  # get on the telegram's official site

uvloop.install()
app = Client(
    'my_account',
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={
        'root': 'plugins'  # {'root': '<folder with plugins>'}
    }
)


def main():
    try:
        print('Running bot...')

        app.run()
    except OperationalError:  # if database is locked
        print('Database is locked! \n')
        print('Please, execute `python userbot.py` again! ')
        
        OS = get_os()  # get your operational system (Windows, Linux, MacOS)

        if OS == 'Linux':
            system('kill -9 $(fuser my_account.session 2>/dev/null)')  # kill python process it locked db
        elif OS == 'Windows':
            # TODO: Check is solution for Windows work
            system('taskkill /F /FI "IMAGENAME eq python.exe" /T')  # kill python process it locked db

    except Exception:
        console.Console().print_exception()  # just beautuful exception
    

def handle_ctrl_z(signal, frame):
    print('Exiting bot...')
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(
        signal.SIGTSTP,
        handle_ctrl_z
    )

    main()
