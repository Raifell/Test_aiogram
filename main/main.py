import asyncio
import logging

from aiogram import F
from aiogram.filters import Command

from config import Config
from text.function import TextFunction
from keyboard.function import Keyboard


class Telebot(Config, TextFunction):
    def __init__(self):
        super().__init__()
        self.markup = Keyboard()
        self.btn_name = ['button 1', 'button 2', 'button 3', 'button 4']

        self.start_action = self.dp.message(Command('start'))(self.start)
        self.help_action = self.dp.message(Command('help'))(self.help)
        self.btn_action = self.dp.message(F.text.lower().in_(self.btn_name))(self.btn)
        self.text_action = self.dp.message()(self.text)

    async def run(self):
        await self.dp.start_polling(self.bot)


async def main():
    logging.basicConfig(level=logging.INFO)
    app = Telebot()
    await app.run()

if __name__ == "__main__":
    asyncio.run(main())
