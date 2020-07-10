import telebot


URL_USD = 'https://banki24.by/minsk/kurs/usd' #Сайт откуда будем брать данные
URL_EUR = 'https://banki24.by/minsk/kurs/eur'
URL_RUB = 'https://banki24.by/minsk/kurs/rub'
TOKEN = '1262379495:AAFeHc0f8Hpv912p1p5M2t4xv-5n-I4uXRE' #Адрес бота, по которому мы с ним будем взаимодейстовать

BOT = telebot.TeleBot(TOKEN)

BUTTON_START = 'В начало'

BUTTON_USD = 'USD'
BUTTON_EUR = 'EUR'
BUTTON_RUB = 'RUB'

BUTTON_GET_ALL_LIST = 'Вывести весь список банков'
BUTTON_BEST_BUY_VALUE = 'Вывести лучший курс для покупки'
BUTTON_BEST_SELL_VALUE = 'Вывести лучший курс для продажи'

def create_keyboard(): #Размещение сообщений
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard

KEYBOARD_START = create_keyboard()
KEYBOARD_START.row(BUTTON_USD, BUTTON_EUR, BUTTON_RUB)


KEYBOARD_CHOICE = create_keyboard()
KEYBOARD_CHOICE.row(BUTTON_GET_ALL_LIST) 
KEYBOARD_CHOICE.row(BUTTON_BEST_BUY_VALUE, BUTTON_BEST_SELL_VALUE) 
KEYBOARD_CHOICE.row(BUTTON_START) 