from os import getenv

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums

import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = getenv('OPENAI_TOKEN')


@Client.on_message(
    filters.command(
        commands=['gpt'],
        prefixes=['.', '/']
    ) & filters.me
)
async def chatGPT(_, message: Message):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'content': message.text, 'role': 'user'}],
        max_tokens=1000,
    )

    await message.reply(
        f'**{response.choices[0].message.content}**',  # `**` for bold text
        parse_mode=enums.ParseMode.MARKDOWN
    )
