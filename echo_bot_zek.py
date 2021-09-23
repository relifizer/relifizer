#import telebot
#
#bot = telebot.TeleBot("1963452899:AAFZXRo8d2ZPLgXGblJZVH2MLzmmvVe2W5Y", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWNimport telebot
#
#bot = telebot.TeleBot("1963452899:AAFZXRo8d2ZPLgXGblJZVH2MLzmmvVe2W5Y")
#
# Подключаем модуль для Телеграма
import telebot


# Указываем токен
bot = telebot.TeleBot('1963452899:AAFZXRo8d2ZPLgXGblJZVH2MLzmmvVe2W5Y')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

# Метод, который получает сообщения и обрабатывает их

    # Если написали «Привет»

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Напиши название региона")
    import sqlite3
    conn = sqlite3.connect('/home/master/mountines.db')
    cur = conn.cursor()
    mesa = message.text
    cur.execute(f"select * from dht where region='{mesa}'")
    d = cur.fetchall()
    bot.send_message(message.from_user.id, f"{d}")

# Обработчик нажатий на кнопки


bot.polling(none_stop=True, interval=0)

