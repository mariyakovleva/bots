# #!/usr/bin/python
# ## -*- coding: utf-8 -*-
import telebot
import config 
import threading 
import buttons
import os 

administrators = (842234154,)
users = {}
users_text = {}
users_text_2 = {}
my_poll = {} 

poll_1 = {} 
poll_2 = {} 
poll_3 = {} 
poll_4 = {} 
poll_5 = {} 
poll_6 = {} 
poll_7 = {} 
poll_8 = {} 
poll_9 = {} 
poll_10 = {} 
poll_11 = {} 
poll_12 = {} 
poll_13 = {} 
poll_14 = {} 
poll_15 = {} 

bot = telebot.TeleBot(config.TOKEN, threaded = True)

@bot.message_handler(commands = ['start'])
def start_msg(message):
    bot.send_message(message.chat.id, 
    f'''*{message.chat.first_name}*! 
    Добро пожаловать в наш бот для оценки качества работы структурных подразделений компании «Транснефтьэнерго»! 📊✨
    Мы стремимся к постоянному совершенствованию и развитию. С помощью этого бота Вы сможете:
        ✅Оценить эффективность работы различных подразделений.
        ✅Поделиться своим мнением и опытом.
    Как это работает:
        🔥Все ответы *анонимны и конфиденциальны*.
        🔥Ваши отзывы помогут нам выявить сильные стороны и области для улучшения.
    Спасибо, что помогаете нам становиться лучше! 🌟
    ''', parse_mode = "Markdown", reply_markup = buttons.Main_menu())


##------ Декоратор (обработчик сообщений) ПОЛЬЗОВАТЕЛЬСКОЙ кливиатуры 
@bot.message_handler(func=lambda message: message.text == 'Оценить подразделение 🏢')
def review_SP(message):
    bot.send_message(message.chat.id, 'Выберите подразделение:', reply_markup = buttons.review_SP())

@bot.message_handler(func=lambda message: message.text == 'Оценить сотрудника 🙎‍♂️')
def write_to_support(message):
    bot.send_message(message.chat.id, 'Пожалуйста, введите ФИО сотрудника, которого Вы бы хотели оценить:')
    users[message.chat.id] = {}
    bot.register_next_step_handler(message, save_msg_text)
 
def save_msg_text(message):
    users[message.chat.id]['emploee'] = message.text
    bot.send_message(message.chat.id, f'Ваши данные успешно сохранены!')

def save_msg_text(message):
    users[message.chat.id]['emploee'] = message.text
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_save = telebot.types.InlineKeyboardButton(text="Сохранить", callback_data='save_data')
    button_change = telebot.types.InlineKeyboardButton(text="Изменить", callback_data='change_data')
    keyboard.add(button_save, button_change)
    bot.send_message(message.chat.id, f'Сохранить данные?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'save_data')
def save_btn(call):
    message = call.message
    message_id = message.message_id
    bot.answer_callback_query(call.id, text="Данные сохранены")
    bot.delete_message(chat_id=message.chat.id, message_id=message_id)
    bot.send_message(message.chat.id, 'Укажите, что Вам понравилось в его/её работе, и что, по Вашему мнению, можно улучшить. Поставьте балл от 1 до 10:')
    bot.register_next_step_handler(message, send_feedback_administrators)

def send_feedback_administrators(message):
    feedback = message.text
    user = users[message.chat.id]
    emploee = user['emploee']
    for admin_chat_id in administrators:
        bot.send_message(admin_chat_id, f'{feedback} оставил мнение сотруднику: {emploee}')
    bot.send_message(message.chat.id, f'Ваши данные успешно *сохранены*!', parse_mode = "Markdown") #reply_markup = ls_keyboards()

@bot.callback_query_handler(func=lambda call: call.data == 'change_data')
def save_btn(call):
    message = call.message
    message_id = message.message_id
    bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text='Изменение данных!')
    write_to_support(message)

@bot.message_handler(func=lambda message: message.text == 'Пройти опрос 📊')
def pool_X(message):
    bot.send_message(message.chat.id, '*Если необходимо отменить голос:*\n\t1. Кликните один раз по голосованию.'\
            '\n\t2. В появившемся меню выберите "Отменить голос".\n\t3. Переголосуйте правильно.', parse_mode = "Markdown")
    if my_poll == {}:
        pool_X = bot.send_poll(message.chat.id, question = f'Обращаетесь ли Вы к ключевым компетенциям сотрудников при использвании 📞Телефонного справочника ТНЭ?',
            options = ['Да', 'Нет'], is_anonymous = 0, allows_multiple_answers = 0)
        my_poll['ls'] = [message.chat.id, pool_X.message_id] 
        # print(my_poll) 
    else: 
        bot.forward_message(message.chat.id, my_poll['ls'][0], my_poll['ls'][1])

@bot.message_handler(func=lambda message: message.text == 'Высказать своё мнение 🙋')
def say_mind(message):
    bot.send_message(message.chat.id, 'Пожалуйста, напишите Ваш отзыв о работе подразделения 🌟\n'
        'Укажите НАЗВАНИЕ ПОДРАЗДЕЛЕНИЯ 💥\n'
        'Что Вам нравится? Что стоит скорректировать? 🤔:')
    users_text[message.chat.id] = {}
    bot.register_next_step_handler(message, send_feedback_administrators_1)

def send_feedback_administrators_1(message):
    users_text[message.chat.id]['usertext'] = message.text
    for admin_chat_id in administrators:
        bot.send_message(admin_chat_id, f'{users_text}')
    bot.send_message(message.chat.id, f'Ваши отзывы важны для нас. Спасибо за ваше участие! 🚀') #reply_markup = ls_keyboards()

@bot.message_handler(func=lambda message: message.text == 'Предложить улучшение 📈')
def add_offer(message):
    bot.send_message(message.chat.id, 'Пожалуйста, напишите Ваши предложения по улучшению работы 📈\n'
        'Мы готовы рассмотреть любые идеи, которые могут повысить эффективность и качество работы:')
    users_text[message.chat.id]= {}
    bot.register_next_step_handler(message, send_feedback_administrators_1)

def send_feedback_administrators_2(message):
    users_text_1[message.chat.id]['usertext'] = message.text
    for admin_chat_id in administrators:
        bot.send_message(admin_chat_id, f'{users_text_1}')
    bot.send_message(message.chat.id, f'Ваш вклад важен для нас. Спасибо за участие! 🚀') #reply_markup = ls_keyboards()

@bot.message_handler(func=lambda message: message.text == 'Посмотреть отчеты 📑')
def sent_develop(message):
    ls_img = {'1': 'Рейтинг клиентоцентричности структурных подразделений Общества', '2': 'Статистика в разрезе месяцев'}
    for key, value in ls_img.items():
        with open((os.path.abspath(f'images/{key}.jpg')), 'rb') as file:
            bot.send_photo(message.chat.id, file.read(), caption = f'{value}')

@bot.message_handler(func=lambda message: message.text == 'Написать разработчику ❓')
def sent_develop(message):
    bot.send_message(message.chat.id, 'Мы будем рады услышать Ваши идеи, комментарии или вопросы✅'
        '\nВсе ваши отзывы помогут нам улучшить работу бота и сделать его еще удобнее🚀'
        '\nКонтакт: @Mari_YakovlevM ')

##------Декоратор (обработчик сообщений) встроенной кливиатуры 
@bot.callback_query_handler(func = lambda msg: True)
def callback_Func(callback_query):
    message = callback_query.message
    text = callback_query.data

    # ------------------------- раздел "Оценить подразделение" ----------------------------
    def pool_review_SP(arg_text, arg_poll_result):
        bot.send_message(message.chat.id, '*Если необходимо отменить голос:*\n\t1. Кликните один раз по голосованию.'\
                '\n\t2. В появившемся меню выберите "Отменить голос".\n\t3. Переголосуйте правильно.', parse_mode = "Markdown")
        if arg_poll_result == {}:
            my_poll = bot.send_poll(message.chat.id, question = f'Реализует ли {arg_text} твои желания?',
                options = ['10 😇', '9 🔥', '8 🤔', '7 😑', '6 🙁', '5 ☹️', '4 😠', '3 😡', '2 🤬'], is_anonymous = 1, allows_multiple_answers = 0)
            arg_poll_result['ls'] = [message.chat.id, my_poll.message_id] 
            # print(my_poll)
        else: 
            bot.forward_message(message.chat.id, arg_poll_result['ls'][0], arg_poll_result['ls'][1])


    if 'ПЭО' in text:
        pool_review_SP(text, poll_1)
   
    if 'СИБ' in text:
        pool_review_SP(text, poll_2)

    if 'ОИ' in text: 
        pool_review_SP(text, poll_3)

    if 'ОСД РРЭ' in text:
        pool_review_SP(text, poll_4)
   
    if 'СПУФ' in text: 
        pool_review_SP(text, poll_5)

    if 'ОБ' in text: 
        pool_review_SP(text, poll_6)

    if 'ОУП' in text: 
        pool_review_SP(text, poll_7)

    if 'ОСД ОРЭ' in text: 
        pool_review_SP(text, poll_8)
       
    if 'СОПТ' in text: 
        pool_review_SP(text, poll_9)

    if 'ОД' in text: 
        pool_review_SP(text, poll_10)

    if 'ОАЗИ' in text: 
        pool_review_SP(text, poll_11)

    if 'СКОВ' in text: 
        pool_review_SP(text, poll_12)
       
    if 'ООПД' in text: 
        pool_review_SP(text, poll_13)

    if 'СЭМ' in text: 
        pool_review_SP(text, poll_14)

    if 'СППБОТ' in text: 
        pool_review_SP(text, poll_15)


# ------------------------------------------------------------------------------------
if __name__ == '__main__':
    def runBot():
        bot.polling(none_stop = True, interval = 0, timeout = 100)

    t1 = threading.Thread(target = runBot)
    t1.start()

