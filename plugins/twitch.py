from aiohttp import ClientSession

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.filters import me, private, command

from fake_useragent import UserAgent


async def get_streamer_url(streamer: str) -> str:
    if 'www.' not in streamer:
        streamer = f'https://www.twitch.tv/{streamer}'
    return streamer


async def is_stream_online(streamer: str) -> bool | None:
    headers = {'User-Agent': UserAgent().random}

    streamer = await get_streamer_url(streamer)

    async with ClientSession(headers=headers) as session:
        async with session.get(url=streamer) as response:
            content = await response.text()

    if streamer not in content:
        return None
    return 'isLiveBroadcast' in content


@Client.on_message(
    command(
        commands=['twitch'],
        prefixes=['/', '.']
    ) & (me | private)
)
async def is_stream_online_(_: Client, message: Message):
    streamer = ''.join(message.command[1:]).replace(' ', '')

    url = await get_streamer_url(streamer)

    is_online = await is_stream_online(streamer)
    streamer_link = f'<a href="{url}">{streamer}</a>'
    if is_online:
        text = f'{streamer_link} is live!'
    elif is_online is None:
        text = f'{streamer} not found!'
    else:
        text = f'{streamer_link} isn\'t live!'

    await message.reply(text)
