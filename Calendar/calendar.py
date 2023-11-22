import telebot
from telebot import types
import calendar
import datetime

from config_data import config

bot = telebot.TeleBot(config.BOT_TOKEN)


class Calendar:
    def __init__(self):
        self.current_date = None
        self.bot = None

    def send_calendar(self, chat_id, check_in_out):
        markup = types.InlineKeyboardMarkup(row_width=7)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        buttons = []
        for day in days:
            buttons.append(types.InlineKeyboardButton(day, callback_data='dummy'))
        markup.row(*buttons)

        # Проверяем, что self.current_date установлено
        if not self.current_date:
            bot.send_message(chat_id, text="Invalid date.")
            return

        # Получаем календарь выбранного месяца и года
        cal = calendar.monthcalendar(self.current_date.year, self.current_date.month)

        # Формируем кнопки для каждой даты в календаре
        for week in cal:
            row = []
            for idx, day in enumerate(week):
                if day == 0:
                    row.append(types.InlineKeyboardButton(" ", callback_data='empty button'))
                else:
                    day_text = str(day)
                    check_date = datetime.datetime(self.current_date.year, self.current_date.month, day)
                    row.append(types.InlineKeyboardButton(day_text, callback_data=f'{check_in_out} '
                                                                                  f'{check_date.day}.'
                                                                                  f'{check_date.month}.'
                                                                                  f'{check_date.year}'))
            markup.row(*row)

        # Заголовок календаря с названием месяца и года
        header = f'{calendar.month_name[self.current_date.month]} {str(self.current_date.year)}'
        # Добавляем кнопки для переключения месяцев
        prev_button = types.InlineKeyboardButton("<<", callback_data='prev_month')
        next_button = types.InlineKeyboardButton(">>", callback_data='next_month')
        markup.row(prev_button, next_button)

        return header, markup


# @bot.callback_query_handler(func=lambda call: True)
def date_callback(call, calendar_instance):
    if call.data == 'empty button':
        pass  # Игнорируем фиктивное нажатие
    elif call.data == 'prev_month':
        prev_month = calendar_instance.current_date.month - 1
        if prev_month == 0:
            prev_month = 12
            prev_year = calendar_instance.current_date.year - 1
        else:
            prev_year = calendar_instance.current_date.year
        calendar_instance.current_date = calendar_instance.current_date.replace(year=prev_year, month=prev_month)
    elif call.data == 'next_month':
        next_month = calendar_instance.current_date.month + 1
        if next_month == 13:
            next_month = 1
            next_year = calendar_instance.current_date.year + 1
        else:
            next_year = calendar_instance.current_date.year
        calendar_instance.current_date = calendar_instance.current_date.replace(year=next_year, month=next_month)
    else:
        bot.send_message(call.from_user.id, text=f'Выбрано: {call.data}')
        bot.answer_callback_query(call.id, text=f'Выбрано: {call.data}')
