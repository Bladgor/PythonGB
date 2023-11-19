import telebot
from datetime import datetime
import calendar

from config_data import config

bot = telebot.TeleBot(config.BOT_TOKEN)


def generate_calendar(year, month):
    cal_text = ''
    cal = calendar.monthcalendar(year, month)

    # Add the header with day names
    cal_text += 'Mo Tu We Th Fr Sa Su\n'

    for week in cal:
        for day in week:
            if day == 0:
                cal_text += '   '
            else:
                cal_text += f'{day:2} '

        cal_text += '\n'

    return cal_text


def create_calendar_markup(year, month):
    markup = telebot.types.InlineKeyboardMarkup(row_width=7)

    # Add buttons for each day of the week
    markup.row(
        *[telebot.types.InlineKeyboardButton(text=calendar.day_abbr[i], callback_data=f'ignore') for i in range(7)])

    # Add buttons for each day in the month
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        for day in week:
            if day == 0:
                markup.add(telebot.types.InlineKeyboardButton(text=' ', callback_data='ignore'))
            else:
                date = datetime(year, month, day)
                markup.add(telebot.types.InlineKeyboardButton(text=str(day),
                                                              callback_data=f'show_date_{date.strftime("%Y-%m-%d")}'))

    # Add navigation buttons for switching months
    markup.row(
        telebot.types.InlineKeyboardButton(text='<< Prev', callback_data='prev_month'),
        telebot.types.InlineKeyboardButton(text='Next >>', callback_data='next_month')
    )

    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! Type /calendar to view the calendar.")


@bot.message_handler(commands=['calendar'])
def send_calendar(message):
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    calendar_text = generate_calendar(current_year, current_month)

    markup = create_calendar_markup(current_year, current_month)

    bot.send_message(message.chat.id, calendar_text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('show_date'))
def show_date_callback(call):
    bot.answer_callback_query(call.id, text=call.data[10:])


@bot.callback_query_handler(func=lambda call: call.data == 'prev_month' or call.data == 'next_month')
def switch_month_callback(call):
    chat_id = call.message.chat.id

    # Extract current year and month from the callback data
    current_year, current_month, _ = call.message.text.split()[3].split('-')
    current_year, current_month = int(current_year), int(current_month)

    # Calculate the new month
    if call.data == 'prev_month':
        new_date = datetime(current_year, current_month, 1) - timedelta(days=1)
    else:
        new_date = datetime(current_year, current_month,
                            calendar.monthrange(current_year, current_month)[1]) + timedelta(days=1)

    new_year, new_month = new_date.year, new_date.month

    # Generate the new calendar and markup
    calendar_text = generate_calendar(new_year, new_month)
    markup = create_calendar_markup(new_year, new_month)

    # Edit the message with the new calendar and markup
    bot.edit_message_text(calendar_text, chat_id, call.message.message_id, reply_markup=markup)


if __name__ == "__main__":
    bot.polling(none_stop=True)
