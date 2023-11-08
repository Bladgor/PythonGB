from telebot.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from loader import bot


@bot.message_handler(commands=['start'])
# @bot.message_handler(content_types=['text'])
def bot_start(message: Message):
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('/low', '/high', '/custom', '/history', '/help')
    # bot.reply_to(message, f"Привет, {message.from_user.full_name}!")
    bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}!\n"
                                           f"Выбери команду", reply_markup=markup)
