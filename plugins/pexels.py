from os import getenv
from random import choice

from pyrogram import Client 
from pyrogram.filters import me, command, private
from pyrogram.types import Message

from aiohttp import ClientSession
from fake_useragent import UserAgent

from dotenv import load_dotenv

from misc.filters import startswith

load_dotenv()


@Client.on_message(
    command(
        commands=['img'],
        prefixes=['.', '/']
    ) & (me | private)
)
async def pexels(_: Client, message: Message) -> None:
    query = ' '.join(message.command[1:])

    headers = {
        'Authorization': getenv('PEXELS_TOKEN'),
        'User-Agent': UserAgent().random
    }
    url = f'https://api.pexels.com/v1/search?query={query}&per_page=10'

    async with ClientSession(headers=headers) as session:
        async with session.get(url=url) as response:
            r = await response.json()
            img_url = choice(r['photos'])['src']['original']
            
    try:
        await message.reply_photo(photo=img_url)
    except:
        await message.reply('Can\'t search image by this query, try again')

