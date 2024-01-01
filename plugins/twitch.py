from aiohttp import ClientSession
from enum import Enum

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.filters import me, private, command

from fake_useragent import UserAgent


class StreamStatus(Enum):
    NOT_FOUND = -1
    OFFLINE = 0
    ONLINE = 1


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
        return StreamStatus.NOT_FOUND
    elif 'isLiveBroadcast' in content:
        return StreamStatus.ONLINE
    else:
        return StreamStatus.OFFLINE


@Client.on_message(
    command(
        commands=['twitch'],
        prefixes=['/', '.']
    ) & (me | private)
)
async def is_stream_online_(_: Client, message: Message):
    streamer = ''.join(message.command[1:]).replace(' ', '')

    url = await get_streamer_url(streamer)

    stream_status = await is_stream_online(streamer)
    streamer_link = f'<a href="{url}">{streamer}</a>'

    match stream_status:
        case StreamStatus.ONLINE:
            text = f'<b>{streamer_link} is live!</b>'
        case StreamStatus.OFFLINE:
            text = f'<b>{streamer_link} isn\'t live!</b>'
        case StreamStatus.NOT_FOUND:
            text = f'<b>{streamer} not found!</b>'

    await message.reply(text)

