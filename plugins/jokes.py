from random import choice

import aiohttp
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command('joke', ['.', '/']))
async def joke(_, message: Message):
    URL = 'https://www.anekdot.ru/release/anekdot/day/'
    headers = {'user-agent': str(UserAgent().random)}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url=URL, headers=headers) as response:
            r = await response.text()

    soup = bs(r, 'lxml')

    joke = choice(
        soup.find_all('div', class_='text')
    ).text
    print(joke)
    await message.reply(joke)
