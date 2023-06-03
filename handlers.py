from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from helpers import *
import subprocess
from aiogram.types import ParseMode
import operator
from functools import reduce, partial
import random

def setup(dp: Dispatcher):
    dp.register_message_handler(bot_help, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())
    dp.register_message_handler(version_call, commands=['version'])
    
    dp.register_message_handler(on_random, commands=['random'])
    dp.register_message_handler(
        message_listener, content_types=types.ContentTypes.ANY)


async def bot_help(msg: types.Message):
    text = [
        'Список команд: ',
        '/random - рандомный мем, который уже мог попадаться в этом чате',
        # '/mem \- рандомный мем, который в этом чате не попадался',
    ]
    
    await msg.reply('\n'.join(text))


async def version_call(msg: types.Message):
    result = subprocess.Popen(
        'git log -1 --pretty="by <b>%cN</b>, %ar%ntitle: %Bcommit: <i>%H</i>"',
        shell=True, stdout=subprocess.PIPE).stdout.read()
    result = result.decode('utf-8', errors='ignore')
    await msg.reply(result, ParseMode.HTML)

shift = -1_000_000_000_000
chat_id = shift - 1175528313

async def on_random(message: types.Message):
    print(message.from_user.mention)
    bot = message.bot
    forward_message_id = get_random_message_id()
    try:
        forward_message = await bot.forward_message(
            chat_id=message.chat.id,
            from_chat_id=chat_id,
            message_id=forward_message_id
        )
    except:
        message.reply('Я упал, попробуй еще раз')

    
def get_random_message_id():
    max_limit = 1404
    result = random.randint(1, max_limit)
    return result

async def message_listener(msg: types.Message):
    print(msg.message_id)
