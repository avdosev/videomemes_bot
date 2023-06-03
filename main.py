from aiogram import Bot, Dispatcher, types, executor

from helpers import *


def on_startup(dp: Dispatcher):
    import handlers
    handlers.setup(dp)


if __name__ == '__main__':
    bot_token = get_bot_token()
    bot = Bot(token=bot_token)
    dp = Dispatcher(bot)
    on_startup(dp)
    print('started...')
    executor.start_polling(dp)
