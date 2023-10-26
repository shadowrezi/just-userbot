from os import getenv, system
from sqlite3 import OperationalError
from platform import system as get_os

from pyrogram import Client

from dotenv import load_dotenv


'''
create a file ".env" (recommended)
and write there your api id and hash, for example:

api_id=123
api_hash=321

WITHOUT WHITESPACE beetween name and value
'''
load_dotenv()

API_ID = getenv('api_id')  # get on the telegram's official site
API_HASH = getenv('api_hash')  # get on the telegram's official site

app = Client(
    'my_account',
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={'root': 'modules'}
)

OS = get_os()  # your operational system (Windows, Linux, MacOS)

while True:
    try:
        app.run()
        break
    except OperationalError:  # if database is locked
        if OS == 'Linux':
            system('kill -9 $(fuser my_account.session 2>/dev/null)')  # only on linux (ubuntu)
        continue
        
        print(
            '''You need to stop previosly python-userbot process!\n
if you use Linux just run this: \n`kill -9 $(fuser my_account.session 2>/dev/null)`
if Windows this (I'm not sure if it will work):\n
`tasklist /FI "IMAGENAME eq my_account.session"` you get PID then:
`taskkill /I /PID <PID>` replace <PID> pid of my_account.session
        '''  # TODO: Check is solution for Windows work
             # TODO: Add solution for Windows in auto-execute
        )
        break
