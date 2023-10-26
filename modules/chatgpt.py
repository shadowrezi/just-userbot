from os import getenv

from pyrogram import Client, filters
from pyrogram import enums

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = getenv('OPENAI_TOKEN')


@Client.on_message(filters.command('gpt', '.') & filters.me)
async def chatGPT(client, msg):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'content': msg.text, 'role': 'user'}],
        max_tokens=1000,
    )
    # print(msg)
    await msg.reply(
        f'**{response.choices[0].message.content}**',  # `**` for bold text
        parse_mode=enums.ParseMode.MARKDOWN
    )
