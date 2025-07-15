from aiogram import types

class Keyboard:
    def __init__(self):
        super().__init__()

        self.button_one = types.KeyboardButton(text="Button 1")
        self.button_two = types.KeyboardButton(text="Button 2")
        self.button_three = types.KeyboardButton(text="Button 3")
        self.button_four = types.KeyboardButton(text="Button 4")

        self.button_group_one = [self.button_one, self.button_two]
        self.button_group_two = [self.button_three, self.button_four]

        self.keyboard = None

    def keyboard_one(self):
        self.keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                      one_time_keyboard=True,
                                                      keyboard=[self.button_group_one])
        return self.keyboard

    def keyboard_two(self):
        self.keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                      one_time_keyboard=True,
                                                      keyboard=[self.button_group_two])
        return self.keyboard

