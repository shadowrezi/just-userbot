from sympy import Symbol, Eq, solve

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.filters import command, me, private


@Client.on_message(
  command(
    commands=['eq'],
    prefixes=['.', '/']
  ) & (me | private)
)
async def equation(_: Client, message: Message):
  text = ' '.join(message.command[1:])
  equation = text.split('=')

  x = Symbol('x')
  y = Symbol('y')
  z = Symbol('z')
  
  eq = Eq(
    eval(equation[0]),
    eval(equation[1])
  )
  result = solve(eq)
  
  await message.reply(
    result[0] if len(result)==1 else result,
    quote=True
  )

@Client.on_message(
  command(
    commands=['math'],
    prefixes=['.', '/']
  ) & (me | private)
)
async def math(_: Client, message: Message):
  text = ' '.join(message.command[1:])
  result = eval(text)

  await message.reply(
    result,
    quote=True
  )
