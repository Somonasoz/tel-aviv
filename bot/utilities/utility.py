# from . import GlobalMessage
from bot.buttons import MultipleRowKeyboard

def msg_introduction_by_lang(lang, messager):
    r_markup = MultipleRowKeyboard()
    msg = messager.get_message("introduction", lang_key=lang)
    sec_msg = messager.get_message("SIM_ask", lang_key=lang)
    _markup = r_markup.get_ReplyButtons(buttons=["yes", "no"], lang_key=lang)
    return msg, sec_msg, _markup

def services_buttons(lang, messager):
    r_markup = MultipleRowKeyboard()
    _markup = r_markup.get_ReplyButtons(buttons=["balance", "tarifs","packages", "services","online_operator", "cancel_button"], lang_key=lang)
    return _markup


def cancel_button(lang):
    r_markup = MultipleRowKeyboard()
    _markup = r_markup.get_ReplyButtons(buttons=["cancel_button"], lang_key=lang)
    return _markup

def close_conversation(lang):
    r_markup = MultipleRowKeyboard()
    _markup = r_markup.get_ReplyButtons(buttons=["close_conversation"], lang_key=lang)
    return _markup