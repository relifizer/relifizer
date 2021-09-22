#import telebot
#
#bot = telebot.TeleBot("1963452899:AAFZXRo8d2ZPLgXGblJZVH2MLzmmvVe2W5Y", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWNimport telebot
#
#bot = telebot.TeleBot("1963452899:AAFZXRo8d2ZPLgXGblJZVH2MLzmmvVe2W5Y")
#

# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telebot


# Указываем токен
bot = telebot.TeleBot('1963452899:AAFZXRo8d2ZPLgXGblJZVH2MLzmmvVe2W5Y')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки для трёх предложений
first = ["Бумажки и дела только у мусоров, у воров закон один - слово..","Фарта, удачи, воровского азарта, а также любви и ложилась, чтоб, карта!","Воровству синоним суицид, проще говоря, воры – самоубийцы.","Для зэков хата – криминальна академия или институт преступных отношений."]
second = ["Ты петух","Пидор","Приятных снов вам босяки, приятных снов вам Воры! А вы сосите мусора, сосите прокуроры!","Святого в этом мире нет, но есть закон, тюрьма и судьи, что загубили жизни цвет, ломая молодые судьбы.", "Чтобы было что пожрать, суетись что есть накрасть."]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Пай-мальчиков и мажоров ждут Оксфорд и рояль. Блатных корешей – алкоголь, сигареты, беспредел и всякая шваль.","Воровские понятия в книгах не писаны – передаются братве по цыганскому радио. Преподают их в тюрьме, зоне, камере и на этапе короли преступного мира.","Закон – тайга, прокурор – медведь.", "Лучше маленькая рыбка, чем большой таракан.","За любовь - любовью, за измену - кровью!", "Дунька-вырви глаз (об энергичной бедовой женщине).", "Хрен на блюде, а не люди."]

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Пидор', callback_data='zodiac')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Ебло', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Хуила', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac": 
        # Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)

