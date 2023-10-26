from os import getenv, system
from sqlite3 import OperationalError

from pyrogram import Client

import openai
from dotenv import load_dotenv


load_dotenv()

openai.api_key = getenv('OPENAI_TOKEN')

api_id = getenv('api_id')
api_hash = getenv('api_hash')

app = Client(
    'my_account',
    api_id=api_id,
    api_hash=api_hash,
    plugins=dict(root='modules')
)
while True:
    try:
        app.run()
        break
    except OperationalError:  # if database is locked
        system('kill -9 $(fuser my_account.session 2>/dev/null)')
        continue

