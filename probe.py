import telebot
from telebot.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from states.contact_information import SearchInfoState
import probe_calendar

message_text = '<pre><code style="font-family: Courier New">Привет, мир!</code></pre>'

token = "5562447993:AAHxkSOD7HsgYawjsfb_wSRI-e9li_xhE6s"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
# @bot.message_handler(content_types=['text'])
def bot_start(message: Message):
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('/low', '/high', '/custom', '/history', '/help')
    # bot.reply_to(message, f"Привет, {message.from_user.full_name}!")
    bot.send_message(message.from_user.id, '<b>Hellow, World!</b>', parse_mode='HTML')
    bot.set_state(message.from_user.id, SearchInfoState.command, message.chat.id)
    probe_calendar.hello(message)


# @bot.message_handler(content_types=['text'])
# def hello(message):
#     markup = InlineKeyboardMarkup(row_width=2)
#     commands = ['low', 'high', 'custom', 'history', 'help']
#     for elem in commands:
#         markup.add(InlineKeyboardButton(
#             text=elem,
#             callback_data=elem
#         ))
#     bot.send_message(message.from_user.id, 'Привет, Мир!', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def my_callback(call):
#     bot.send_message(call.from_user.id, f'Выбрано {call.data}')


bot.polling()
