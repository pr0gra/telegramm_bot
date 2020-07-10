from settings.SETTINGS import * #Импорт всех данных из сеттингс.пай

from parse.Parse import Parse #Импортируем метод Парсе.пай

from parse.dataPy import Data

import telebot






@BOT.message_handler(commands = ['start'])
def start_message(message):
    BOT.send_message(message.chat.id, 'Выберете интересующую вас валюту', reply_markup = KEYBOARD_START)

@BOT.message_handler(content_types=['text'])
def get_text_messages(message):

    global site, values
    
    if message.text == BUTTON_USD:
        site = Parse(URL_USD).get_content()
        BOT.send_message(message.chat.id, 'Что вас интересует', reply_markup = KEYBOARD_CHOICE)

    elif message.text == BUTTON_EUR:
        site = Parse(URL_EUR).get_content()
        BOT.send_message(message.chat.id, 'Что вас интересует', reply_markup = KEYBOARD_CHOICE)

    elif message.text == BUTTON_RUB:
        site = Parse(URL_RUB).get_content()
        BOT.send_message(message.chat.id, 'Что вас интересует', reply_markup = KEYBOARD_CHOICE)


    elif message.text == BUTTON_GET_ALL_LIST:
        values = Data(site)
        BOT.send_message(message.chat.id, values.get_all_list(), reply_markup =KEYBOARD_CHOICE)
    
    elif message.text == BUTTON_BEST_BUY_VALUE:
        values = Data(site)
        BOT.send_message(message.chat.id, values.best_buy_value, reply_markup = KEYBOARD_CHOICE)
    
    elif message.text == BUTTON_BEST_SELL_VALUE:
        values = Data(site)
        BOT.send_message(message.chat.id, values.best_sell_value, reply_markup = KEYBOARD_CHOICE)

    elif message.text == BUTTON_START:
        start_message(message)

    else:
        BOT.send_message(message.chat.id, 'Я тебя не понимаю, введи /start')

BOT.polling()
