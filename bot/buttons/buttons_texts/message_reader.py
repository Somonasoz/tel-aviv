
import os
import json
path = os.getcwd()

class ButtonsMessage:
    def init_file(self):
        f = open(path+"/bot/buttons/buttons_texts/messages.json","r", encoding='utf-8')
        data = json.load(f)
        return data

    def get_message(self, key_value, lang_key=None):
        if lang_key is None:
            data = self.init_file()["messages"][key_value]
        else:
            data = self.init_file()["messages"][lang_key][key_value]
        return data if data is not None else None
