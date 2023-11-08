from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from loader import bot


@bot.message_handler(commands=['history'])
def survey(message: Message) -> None:
    bot.send_message(message.from_user.id, f'',
                                           reply_markup=ReplyKeyboardRemove())


