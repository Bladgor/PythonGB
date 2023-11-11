from telebot.types import Message, ReplyKeyboardMarkup

from loader import bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@bot.message_handler(state=None)
def bot_echo(message: Message):
    bot.reply_to(message, "Я тебя не понимаю.\nСообщение: "
                          f"{message.text}")
    markup = ReplyKeyboardMarkup().add('/start')
    bot.send_message(message.from_user.id, 'Для запуска бота нажми кнопку "/start"', reply_markup=markup)
