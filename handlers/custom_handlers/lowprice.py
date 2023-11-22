import datetime
from telebot.types import (Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from loader import bot
from states.contact_information import SearchInfoState
from database.data_processing import database_handler
from api_request import search_id_location
from Calendar.calendar import Calendar


keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
calendar_instance = Calendar()
current_date = datetime.datetime.now()  # Установить начальную дату на текущий день текущего месяца
calendar_instance.current_date, calendar_instance.bot = current_date, bot


def keyboard_numbers(numbers):
    markup = ReplyKeyboardMarkup(row_width=5, resize_keyboard=True)
    row = [KeyboardButton(x) for x in numbers]
    markup.add(*row)

    return markup


def city_markup(city):
    cities = search_id_location(city)
    destinations = InlineKeyboardMarkup()
    for city in cities:
        destinations.add(InlineKeyboardButton(
            text=city,
            callback_data=f'id {cities[city]}'))

    return destinations


@bot.message_handler(commands=['low', 'high', 'custom'])
def survey(message: Message) -> None:
    bot.send_message(message.from_user.id, f'В каком городе будет проводиться поиск?',
                                           reply_markup=ReplyKeyboardRemove())

    bot.set_state(message.from_user.id, SearchInfoState.specify, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['command'] = message.text


@bot.message_handler(state=SearchInfoState.specify)
def get_city(message: Message) -> None:
    flag = True
    if len(message.text.split(' ')) == 1:
        if message.text.find('-'):
            for elem in message.text.split('-'):
                if not elem.isalpha():
                    flag = False
    else:
        for elem in message.text.split(' '):
            if not elem.isalpha():
                flag = False
    if flag:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['city'] = message.text.title()
        bot.send_message(message.from_user.id, 'Уточните, пожалуйста:', reply_markup=city_markup(message.text.title()))
    else:
        bot.send_message(message.from_user.id, 'Город может содержать только буквы.')


@bot.callback_query_handler(func=lambda call: 'prev_month' in call.data or 'next_month' in call.data)
def switch_months_callback(call):
    if call.data == 'prev_month':
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

    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        check = 'check_out' if 'check_in' in data else 'check_in'

    header, markup = calendar_instance.send_calendar(call.message.chat.id, check_in_out=f'{check}')
    if check == 'check_in':
        select_a_date = 'Выберите дату заезда'
    else:
        select_a_date = 'Выберите дату выезда'
    bot.send_message(call.from_user.id, text=f"{select_a_date}:\n{header}", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: 'id' in call.data)
def check_in_callback(call):
    header, markup = calendar_instance.send_calendar(call.message.chat.id, check_in_out='check_in')
    bot.send_message(call.from_user.id, text=f"Выберите дату заезда:\n{header}", reply_markup=markup)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['city_id'] = call.data.split(' ')[1]


@bot.callback_query_handler(func=lambda call: 'check_in' in call.data)
def check_out_callback(call):
    today = datetime.datetime.now()
    check_in_date = list(map(int, (call.data.split(' ')[1]).split('.')))
    selected_date = datetime.datetime(check_in_date[2],
                                      check_in_date[1],
                                      check_in_date[0])
    if selected_date < today:
        header, markup = calendar_instance.send_calendar(call.message.chat.id, check_in_out='check_in')
        bot.send_message(call.from_user.id,
                         text=f"Дата не может быть прошедшей!\n"
                              f"Выберите дату заезда:\n{header}",
                         reply_markup=markup)
    else:
        header, markup = calendar_instance.send_calendar(call.message.chat.id, check_in_out='check_out')
        bot.send_message(call.from_user.id,
                         text=f"Отлично!\nТеперь выберите дату выезда:\n{header}",
                         reply_markup=markup)
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            data['check_in'] = call.data.split(' ')[1]


@bot.callback_query_handler(func=lambda call: 'check_out' in call.data)
def choice_callback(call):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        check_in_date = list(map(int, data['check_in'].split('.')))
        check_in_date = datetime.datetime(check_in_date[2], check_in_date[1], check_in_date[0])
    check_out_date = list(map(int, (call.data.split(' ')[1]).split('.')))
    selected_date = datetime.datetime(check_out_date[2],
                                      check_out_date[1],
                                      check_out_date[0])
    if selected_date <= check_in_date:
        header, markup = calendar_instance.send_calendar(call.message.chat.id, check_in_out='check_out')
        bot.send_message(call.from_user.id,
                         text=f"Дата выезда не может быть раньше или равной дате заезда!\n"
                              f"Выберите дату выезда:\n{header}",
                         reply_markup=markup)
    else:
        bot.send_message(call.from_user.id, 'Сколько отелей вывести? (от 1 до 10)',
                         reply_markup=keyboard_numbers(keys))
        bot.set_state(call.from_user.id, SearchInfoState.hotels_quantity, call.message.chat.id)
        data['check_out'] = call.data.split(' ')[1]


@bot.message_handler(state=SearchInfoState.hotels_quantity)
def get_hotels_quantity(message: Message) -> None:
    if message.text.isdigit() and 0 < int(message.text) < 11:
        markup_yes_no = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        markup_yes_no.add('Да', 'Нет')
        bot.send_message(message.from_user.id, 'Вывести фотографии? Да/Нет', reply_markup=markup_yes_no)
        bot.set_state(message.from_user.id, SearchInfoState.confirm_photo, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['hotels_quantity'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Введите количество отелей (от 1 до 10).',
                         reply_markup=keyboard_numbers(keys))


@bot.message_handler(state=SearchInfoState.confirm_photo)
def get_confirm_photo(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['confirm_photo'] = message.text
    if message.text.title() == 'Да':
        bot.send_message(message.from_user.id, 'Сколько фотографий вывести? (от 1 до 10)',
                         reply_markup=keyboard_numbers(keys))
        bot.set_state(message.from_user.id, SearchInfoState.photo_quantity, message.chat.id)

    else:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['photo_quantity'] = 0

        database_handler(message.from_user.full_name, data)

        text = f'Спасибо за предоставленную информацию. Ваши данные:\n' \
               f'Город: {data["city"]}\n' \
               f'Кол-во отелей: {data["hotels_quantity"]}\n' \
               f'Вывод фото: {data["confirm_photo"]}\n' \
               f'Кол-во фото: {data["photo_quantity"]}\n'
        bot.send_message(message.from_user.id, text, reply_markup=ReplyKeyboardRemove())
        bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state=SearchInfoState.photo_quantity)
def get_photo_quantity(message: Message) -> None:
    if message.text.isdigit() and 0 < int(message.text) < 11:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['photo_quantity'] = message.text

        database_handler(message.from_user.full_name, data)

        text = f'Спасибо за предоставленную информацию. Ваши данные:\n' \
               f'Город: {data["city"]}\n' \
               f'Кол-во отелей: {data["hotels_quantity"]}\n' \
               f'Вывод фото: {data["confirm_photo"]}\n' \
               f'Кол-во фото: {data["photo_quantity"]}\n'
        bot.send_message(message.from_user.id, text, reply_markup=ReplyKeyboardRemove())
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.from_user.id, 'Введите количество фотографий (от 1 до 10).',
                         reply_markup=keyboard_numbers(keys))
