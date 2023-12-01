import datetime
from telebot.types import (Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,
                           InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto)
from loader import bot
from states.contact_information import SearchInfoState
from database.data_processing import database_handler
from api_request import search_id_location, search_hotels
from Calendar.calendar import Calendar

keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
star = '\u2B50'
calendar_instance = Calendar()
current_date = datetime.datetime.now()  # Установить начальную дату на текущий день текущего месяца
calendar_instance.current_date, calendar_instance.bot = current_date, bot


def date_str_to_datetime(date_text):
    date_text = list(map(int, date_text.split('.')))
    date_text = datetime.date(date_text[2], date_text[1], date_text[0])

    return date_text


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


def add_photo_to_media(photos_list, text, quant_photo):
    media = []
    for index, photo in enumerate(photos_list):
        if index == quant_photo:
            break
        if index == 0:
            media.append(InputMediaPhoto(photo, caption=text, parse_mode='HTML'))
        else:
            media.append(InputMediaPhoto(photo))

    return media


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
    today = datetime.datetime.today().date()
    check_in_date = list(map(int, (call.data.split(' ')[1]).split('.')))
    selected_date = datetime.datetime(check_in_date[2],
                                      check_in_date[1],
                                      check_in_date[0]).date()
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
        check_in_date = datetime.datetime(check_in_date[2],
                                          check_in_date[1],
                                          check_in_date[0]).date()
    check_out_date = list(map(int, (call.data.split(' ')[1]).split('.')))
    selected_date = datetime.datetime(check_out_date[2],
                                      check_out_date[1],
                                      check_out_date[0]).date()
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
        bot.send_message(message.from_user.id, 'Сколько вывести фотографий для каждого отеля? (от 1 до 10)',
                         reply_markup=keyboard_numbers(keys))
        bot.set_state(message.from_user.id, SearchInfoState.photo_quantity, message.chat.id)

    else:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['photo_quantity'] = 0

        text = (f'Спасибо за обращение. Ваш запрос обрабатывается.\n'
                f'Пожалуйста, подождите...')
        bot.send_message(message.from_user.id, text, reply_markup=ReplyKeyboardRemove())

        database_handler(message.from_user.full_name, data)

        check_in = date_str_to_datetime(data['check_in'])
        check_out = date_str_to_datetime(data['check_out'])
        quantity_days = (check_out - check_in).days
        hotels = search_hotels(city_id=data['city_id'],
                               check_in=check_in,
                               check_out=check_out,
                               quant_photo=data['photo_quantity'])
        index = 1
        for hotel in hotels:
            price = round(hotel[1]["price"], 2)
            distance_to_the_center = round((hotel[1]["to_the_center"] * 0.62137), 2)
            information = (f'Название отеля: <b>{hotel[0]}</b>\n'
                           f'Рейтинг: <b>{hotel[1]["rating"]}</b>'
                           f'Цена за ночь: <b>${price}</b>\n'
                           f'За выбранный период \n'
                           f'c "{check_in.strftime("%d %b %Y")}" '
                           f'по "{check_out.strftime("%d %b %Y")}": '
                           f'<b>${quantity_days * price}</b>\n'
                           f'До центра: <b>{distance_to_the_center} км</b>\n'
                           f'Подробнее: '
                           f'https://www.hotels.com/h{hotel[1]["hotel_id"]}.Hotel-Information')

            bot.send_message(message.from_user.id, information, parse_mode='HTML')
            index += 1
            if index > int(data["hotels_quantity"]):
                break
        bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state=SearchInfoState.photo_quantity)
def get_photo_quantity(message: Message) -> None:
    if message.text.isdigit() and 0 < int(message.text) < 11:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['photo_quantity'] = message.text

        database_handler(message.from_user.full_name, data)

        text = (f'Спасибо за обращение. Ваш запрос обрабатывается.\n'
                f'Пожалуйста, подождите...')
        bot.send_message(message.from_user.id, text, reply_markup=ReplyKeyboardRemove())
        if data['command'] == '/low':
            check_in = date_str_to_datetime(data['check_in'])
            check_out = date_str_to_datetime(data['check_out'])
            quantity_days = (check_out - check_in).days
            hotels = search_hotels(city_id=data['city_id'],
                                   check_in=check_in,
                                   check_out=check_out,
                                   quant_photo=data['photo_quantity'])
            index = 1
            for hotel in hotels:
                price = round(hotel[1]["price"], 2)
                distance_to_the_center = round((hotel[1]["to_the_center"] * 0.62137), 2)
                information = (f'Название отеля: <b>{hotel[0]}</b>\n'
                               f'Рейтинг: <b>{hotel[1]["rating"]}</b>\n'
                               f'Цена за ночь: <b>${price}</b>\n'
                               f'За выбранный период \n'
                               f'c "{check_in.strftime("%d %b %Y")}" '
                               f'по "{check_out.strftime("%d %b %Y")}": '
                               f'<b>${quantity_days * price}</b>\n'
                               f'До центра: <b>{distance_to_the_center} км</b>\n'
                               f'Подробнее: '
                               f'https://www.hotels.com/h{hotel[1]["hotel_id"]}.Hotel-Information')
                media_group = add_photo_to_media(hotel[1]['photos'], information, int(data["photo_quantity"]))

                bot.send_media_group(message.from_user.id, media=media_group)
                index += 1
                if index > int(data["hotels_quantity"]):
                    break
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.from_user.id, 'Введите количество фотографий для каждого отеля (от 1 до 10).',
                         reply_markup=keyboard_numbers(keys))


# @bot.message_handler(state=SearchInfoState.command)
# def command(message):
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         selected_command = data['command']
#     bot.send_message(message.from_user.id, selected_command)
