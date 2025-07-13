from aiogram import types

class Keyboard:
    def __init__(self):
        super().__init__()

        self.button_one = types.KeyboardButton(text="Button 1")
        self.button_two = types.KeyboardButton(text="Button 2")

        self.button_group_one = [self.button_one, self.button_two]

        self.keyboard_one = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                      one_time_keyboard=True,
                                                      keyboard=[self.button_group_one])
