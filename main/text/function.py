from aiogram import types


class TextFunction:

    async def text(self, message: types.Message):
        if message.text == 't':
            await self.bot.send_message(
                chat_id=message.chat.id,
                text=message.text,
                reply_to_message_id=message.message_id
            )
        else:
            await self.bot.send_message(
                chat_id=message.chat.id,
                text=message.text
            )

    async def start(self, message: types.Message):
        await self.bot.send_message(
            chat_id=message.chat.id,
            text='Hello {}'.format(message.from_user.full_name),
            reply_markup=self.markup.keyboard_one
        )

    async def help(self, message: types.Message):
        await self.bot.send_message(
            chat_id=message.chat.id,
            text='Test echo bot'
        )

    async def btn_1(self, message: types.Message):
        await self.bot.send_message(
            chat_id=message.chat.id,
            text='detect button 1'
        )

    async def btn_2(self, message: types.Message):
        await self.bot.send_message(
            chat_id=message.chat.id,
            text='detect button 2'
        )