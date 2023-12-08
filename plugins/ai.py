from pyrogram import Client, filters
from pyrogram.types import Message

from g4f import Provider
from g4f.Provider import ChatgptAi, Bing

context = [
    {
        'role': 'user',
        'content': 'Format your answers, but i will use you for telegram bot and this text for telegram, for example: **TEXT**'
    }
]


async def ai(message: Message, provider: Provider, tone: str|None=None):
    global context

    context.append(
        {
            'role': 'user',
            'content': message.text
        }
    )

    kwargs = {
        'model': 'gpt-3.5-turbo',
        'messages': context
    }
    
    if tone:
        kwargs['tone'] = tone

    response = await provider.create_async(**kwargs)
    print(response)
    await message.reply(
        response
    )


@Client.on_message(
    filters.command(
        commands=['gpt'],
        prefixes=['.', '/']
    ) & filters.me
)
async def chatGPT(_, message: Message):
    await ai(message, ChatgptAi)



@Client.on_message(
    filters.command(
        commands=['bing'],
        prefixes=['.', '/']
    ) & filters.me
)
async def bing(_, message: Message):
    await ai(message, Bing, tone='Balanced')
