from aiogram.dispatcher.filters.state import State, StatesGroup
from bot import dp, languales_menu, GlobalMessage, store, Fetcher, msg_introduction_by_lang, \
    close_conversation, cancel_button, services_buttons, bot, ButtonsMessage
from aiogram import types, executor
from aiogram.dispatcher import FSMContext
from bot.core import GROUP_ID
#ali
def phone_is_valid(value):
    import re
    is_number = bool(re.match('^[0-9]+$', value))
    if is_number:
        fetcher = Fetcher()
        res = fetcher.get_phone(value)
        return res

    return is_number


messager = GlobalMessage()
button_messager = ButtonsMessage()

my_tarif = store.tarif or None  #current tarif

class Form(StatesGroup):
    has_phone = State()
    phone = State()
    choosed_tarif = State()
    conversation_closed = State()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    msg = messager.get_message("wellcome")
    await message.answer(msg, reply_markup=languales_menu)



@dp.message_handler(commands=['test'])
async def send_test(message: types.Message):
    await bot.forward_message(GROUP_ID, message.chat.id, message_id=message.message_id)



@dp.message_handler(lambda message: message.text in ['TJ', 'RU','ENG'])
async def send_welcome_by_lang(message: types.Message):
    store.lang = message.text.lower()
    sender_welcome_by_lang = msg_introduction_by_lang(store.lang, messager)
    msg = sender_welcome_by_lang[0]
    sec_msg = sender_welcome_by_lang[1]
    _markup = sender_welcome_by_lang[2]
    await Form.has_phone.set()
    await message.answer(f"{msg}\n")
    await message.answer(f"{sec_msg}\n", reply_markup=_markup)


# @dp.message_handler()
@dp.message_handler(lambda message: message.text in ["Отмена", "Cancel", "Анчоми сухбат", "Close conversation",
                                "Завершить беседу", "Баргаштан"], state='*',content_types=types.ContentTypes.ANY)
async def canceling(message:types.Message, state=FSMContext):
    await state.finish()
    await bot.send_message(message.chat.id, message.text, reply_markup=types.ReplyKeyboardRemove())

#istifoda sim card
@dp.message_handler(state=Form.has_phone)
async def send_reset(message: types.Message, state=FSMContext):
    print(message.text)
    positive_answer = button_messager.get_message("yes", store.lang)
    negative_answer = button_messager.get_message("no", store.lang)
    if message.text == positive_answer:
        await Form.phone.set()
        msg = messager.get_message("enter_your_phone", lang_key=store.lang)
        return await message.answer(msg, parse_mode="Markdown", reply_markup=cancel_button(store.lang))
    elif message.text == negative_answer:
        await state.finish( )
        msg = messager.get_message("go_to", lang_key=store.lang)
        return await message.answer(msg, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
    else:
        msg = messager.get_message("err_use_sim_card", store.lang)
        return await message.answer(msg, parse_mode="Markdown")


@dp.message_handler(lambda message: not phone_is_valid(message.text), state=Form.phone)
async def process_phone_invalid(message:types.Message):
    msg = messager.get_message("enter_your_phone2", lang_key=store.lang)
    return await message.reply(msg, reply_markup=cancel_button(store.lang))

@dp.message_handler(lambda message: phone_is_valid(message.text), state=Form.phone)
async def process_phone_invalid(message:types.Message, state=FSMContext):
    r_buttons = services_buttons(store.lang, messager)
    await state.finish()
    return await message.answer("✅", reply_markup=r_buttons)


@dp.message_handler(lambda message: message.text in ["Balance", "Tarifs", "Packages", "Services",
"Online operator", "Баланс","Мой Тариф", "Пакеты", "Услуги", "Онлайн консультант",
    "Тавозун" , "Тарифхо", "Бастаҳо","Хизматрасонихо","Тамос бо амалгар" ])
async def canceling(message:types.Message):
    _balance = button_messager.get_message("balance", store.lang)
    _tarifs = button_messager.get_message("tarifs", store.lang)
    _packages = button_messager.get_message("packages", store.lang)
    _services = button_messager.get_message("services", store.lang)
    _online_operator = button_messager.get_message("online_operator", store.lang)



    if message.text == _balance:
        msg = messager.get_message("balance",lang_key=store.lang)
        info_msg = f"{msg} {str(store.tarif.userBalance) or ''}"
        await message.answer(info_msg, parse_mode="Markdown")


    elif message.text == _tarifs:
        msg = messager.get_message("tarifs",lang_key=store.lang)
        info_msg = f"{msg} {str(store.tarif.userTariff) or ''}"
        await message.answer(info_msg, parse_mode="Markdown")



    elif message.text == _packages:
        msg = messager.get_message("packages", lang_key=store.lang)
        info_msg = f"{msg} {str(store.tarif.userMsisdn) or ''}"
        await message.answer(info_msg, parse_mode="Markdown")


    elif message.text == _services:
        msg = messager.get_message("services", lang_key=store.lang)
        info_msg = f"{msg}"
        await message.answer(info_msg, parse_mode="Markdown")


    elif message.text == _online_operator:
        msg = messager.get_message("online_operator",lang_key=store.lang)
        info_msg = msg
        await Form.conversation_closed.set()
        await message.answer(info_msg, parse_mode="Markdown", reply_markup=close_conversation(store.lang))

@dp.message_handler()
async def echo(message: types.Message):
    msg = f"{message['from']['first_name']}: {message.text}"
    await bot.send_message(message.reply_to_message.forward_from.id, msg , parse_mode="Markdown")

@dp.message_handler(state=Form.conversation_closed)
async def conversation(message:types.Message):
    await bot.forward_message(GROUP_ID, message.chat.id, message_id=message.message_id)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
