from aiogram.types.reply_keyboard import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
    KeyboardButtonPollType
)



from .buttons_texts import ButtonsMessage

button_message = ButtonsMessage()

taj_button = KeyboardButton('TJ')
eng_button = KeyboardButton('ENG')
run_button = KeyboardButton('RU')


languales_menu = ReplyKeyboardMarkup(resize_keyboard=True)
languales_menu.add(taj_button, run_button, eng_button)




class MultipleRowKeyboard:

    def __init__(self):
        pass

    def get_ReplyButtons(self, buttons:list, lang_key)->ReplyKeyboardMarkup:
        _buttons = []
        replay_markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for item in buttons:
            msg = button_message.get_message(item, lang_key=lang_key)
            _buttons.append(KeyboardButton(msg))
        for button in _buttons:
            replay_markup.row(button)
        return replay_markup