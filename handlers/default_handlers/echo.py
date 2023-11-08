from telebot.types import Message, ReplyKeyboardMarkup

from loader import bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@bot.message_handler(state=None)
def bot_echo(message: Message):
    bot.reply_to(message, "Эхо без состояния или фильтра.\nСообщение: "
                          f"{message.text}")
    markup = ReplyKeyboardMarkup()
    markup.add('/start')
    bot.send_message(message.from_user.id, 'Для запуска бота нажми кнопку "/start"', reply_markup=markup)
