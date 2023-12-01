import datetime
import telebot

# Создание экземпляра бота
bot = telebot.TeleBot('5562447993:AAHxkSOD7HsgYawjsfb_wSRI-e9li_xhE6s')


@bot.message_handler(commands=['start'])
def send_rating(message):
    star = '\u2B50'

    text = (f'Название отеля:  <b>Quality Inn Terre Haute University Area</b>\n'
            f'Рейтинг:  <b>7.5</b> {star}\n'
            f'Цена за ночь:  <b>$66</b>\n'
            f'За выбранный период\n'
            f'c "01 Dec 2023" по "03 Dec 2023":  <b>$132</b>\n'
            f'До центра:  <b>11.34 км</b>\n'
            f'Подробнее:  https://www.hotels.com/h36314.Hotel-Information')

    bot.send_message(message.chat.id, text, parse_mode='HTML')


bot.polling()
