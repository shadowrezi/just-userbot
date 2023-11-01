import json

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(
        commands=['set'],
        prefixes=['.', '/']
    ) & filters.me,
    group=-1
)
async def add_variable(_, message: Message):  # .set key=value
    text = ' '.join(message.command[1:])
    
    text_ = text.split('=')
    
    key = text_[0]
    value = ' '.join(text_[1:])
    
    with open('data.json', 'r+') as f:
        file_data = json.load(f)

        file_data[key] = value

        f.seek(0)

        json.dump(file_data, f, indent=4)


@Client.on_message(
    filters.command(
        commands=['get'],
        prefixes=['.', '/'],
    ) & filters.me,
    group=-1
)
async def get_variable(_, message: Message):
    key = ' '.join(message.command[1:])
    
    with open('data.json', 'r') as f:
        data = json.load(f)
        
        if key not in data.keys() or (data[key] is None):
            await message.reply('**Enter a correct variable name!**')
        else:
            await message.reply(data[key], quote=True)


@Client.on_message(
    filters.command(
        commands=['delete'],
        prefixes=['.', '/']
    ) & filters.me,
    group=-1
)
async def delete_variable(_, message: Message):
    key = ' '.join(message.command[1:])
    
    with open('data.json', 'r+') as f:
        file_data = json.load(f)

        file_data[key] = None

        f.seek(0)

        json.dump(file_data, f, indent=4)
