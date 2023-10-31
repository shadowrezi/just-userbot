from os import getenv

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums

import openai
from openai.error import AuthenticationError, RateLimitError

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
    if not openai.api_key:  # if openai api key isn't in file `.env`
        await message.reply(
            '**Add your openai api key to file `.env`**'
        )
        return

    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'content': message.text, 'role': 'user'}],
            max_tokens=1000,
        )

        await message.reply(
            f'**{response.choices[0].message.content}**',  # `**` for bold text
            parse_mode=enums.ParseMode.MARKDOWN
        )
    except AuthenticationError:  # if your openai api key is incorrect
        await message.reply(
            '**Your openai api key is incorrect! **',
            quote=True
        )
    except RateLimitError:
        await message.reply(
            '**You exceeded your current quota, please check your plan and billing details! **',
            quote=True
        )
