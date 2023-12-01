import telebot
from telebot.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from states.contact_information import SearchInfoState

message_text = '<pre><code style="font-family: Courier New">Привет, мир!</code></pre>'

token = "5562447993:AAHxkSOD7HsgYawjsfb_wSRI-e9li_xhE6s"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def hello(message):
    markup = InlineKeyboardMarkup()
    commands = ['low', 'high', 'custom', 'history', 'help']
    for elem in commands:
        markup.add(InlineKeyboardButton(
            text=elem,
            callback_data=elem
        ))

    star = '\u2B50'
    print(star, type(star))
    bot.send_message(message.from_user.id, f'Привет, Мир!{star}', parse_mode='HTML')


bot.polling()
