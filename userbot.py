from os import getenv, system
from sqlite3 import OperationalError
from platform import system as get_os

import rich

from pyrogram import Client

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

app = Client(
    'my_account',
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={'root': 'modules'}
)

OS = get_os()  # your operational system (Windows, Linux, MacOS)


def main():
    try:
        print('Running bot...')
        app.run()
    except OperationalError:  # if database is locked
        print('Database is locked! ')
        print('Please, execute `python userbot.py` again! ')

        if OS == 'Linux':
            system('kill -9 $(fuser my_account.session 2>/dev/null)')  # only on linux (ubuntu)
        elif OS == 'Windows':
            # TODO: Check is solution for Windows work
            system('taskkill /F /FI "IMAGENAME eq python.exe" /T')
    
    except Exception:
        rich.Console().print_exception()  # just beautuful exception


if __name__ == '__main__':
    main()
