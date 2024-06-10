

from telebot import types #клавиатура

#----------------        пользовательские кнопки      -----------------------

def Main_menu():
     Main_menu = types.ReplyKeyboardMarkup (resize_keyboard = False, row_width = 2)
     ls_menu = ['Оценить подразделение 🏢',
                'Оценить сотрудника 🙎‍♂️',
                'Пройти опрос 📊',
                'Высказать своё мнение 🙋',
                'Предложить улучшение 📈',
                'Посмотреть отчеты 📑',
                'Написать разработчику ❓' 
                ] 
     Main_menu.add(*[types.KeyboardButton (menu) for menu in ls_menu])
     return Main_menu


#----------------         встроенные кнопки    -----------------------

def review_SP(): 
     review_SP = types.InlineKeyboardMarkup(row_width = 3) 
     ls_review_SP = [ 
          types.InlineKeyboardButton('ПЭО', callback_data = 'ПЭО'),
          types.InlineKeyboardButton('СИБ', callback_data = 'СИБ'),
          types.InlineKeyboardButton('ОИ', callback_data = 'ОИ'),
          types.InlineKeyboardButton('ОСД РРЭ', callback_data = 'ОСД РРЭ'),
          types.InlineKeyboardButton('СПУФ', callback_data = 'СПУФ'),
          types.InlineKeyboardButton('ОБ', callback_data = 'ОБ'),
          types.InlineKeyboardButton('ОУП', callback_data = 'ОУП'),
          types.InlineKeyboardButton('ОСД ОРЭ', callback_data = 'ОСД ОРЭ'),
          types.InlineKeyboardButton('СОПТ', callback_data = 'СОПТ'),
          types.InlineKeyboardButton('ОД', callback_data = 'ОД'),
          types.InlineKeyboardButton('ОАЗИ', callback_data = 'ОАЗИ'),
          types.InlineKeyboardButton('СКОВ', callback_data = 'СКОВ'),
          types.InlineKeyboardButton('ООПД', callback_data = 'ООПД'),
          types.InlineKeyboardButton('СЭМ', callback_data = 'СЭМ'),
          types.InlineKeyboardButton('СППБОТ', callback_data = 'СППБОТ')
          ]
     review_SP.add(*ls_review_SP)
     return review_SP
