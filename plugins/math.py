from sympy import Symbol, Eq, solve
from re import compile, fullmatch

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.filters import command, me, private


def is_number(num: str) -> bool:
  pattern = compile(r'\d+(\.\d+)?')
  return bool(
    fullmatch(pattern, num)
  )


async def replace_letters(text: str, letters: list[str]='xyz'):
  result = text
  for letter in letters:
      for i in range(1, len(text)):
          if text[i] in letters and is_number(text[i - 1]):
              result.replace(letter, '*' + letter, 1)
  return result


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

  eq1 = eval(await replace_letters(equation[0]))
  eq2 = eval(await replace_letters(equation[0]))
  
  eq = Eq(
    eq1,
    eq2
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
