from os import getenv, system
from sqlite3 import OperationalError
from platform import system as get_oc

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

api_id = getenv('api_id')  # get on the telegram's official site
api_hash = getenv('api_hash')  # get on the telegram's official site

app = Client(
    'my_account',
    api_id=api_id,
    api_hash=api_hash,
    plugins={'root': 'modules'}
)

oc = get_oc()

while True:
    try:
        app.run()
        break
    except OperationalError:  # if database is locked
        if oc == 'Linux':
            system('kill -9 $(fuser my_account.session 2>/dev/null)')  # only on linux (ubuntu)
            continue
        break  # if oc isn't Linux
