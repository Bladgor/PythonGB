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
        print(elem, type(elem))
        markup.add(InlineKeyboardButton(
            text=elem,
            callback_data=elem
        ))
    msg = bot.send_message(message.from_user.id, 'Привет, Мир!', reply_markup=markup)
    bot.register_next_step_handler(msg, send)


@bot.callback_query_handler(func=lambda call: True)
def my_callback(call):
    bot.send_message(call.from_user.id, f'Выбрано {call.data}')


@bot.message_handler(content_types=['text'])
def send(message):
    bot.send_message(message.from_user.id, 'Конец!')
