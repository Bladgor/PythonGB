from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from loader import bot
from states.contact_information import SearchInfoState
from database.data_processing import database_handler


keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


def keyboard(numbers):
    markup = ReplyKeyboardMarkup(row_width=5, resize_keyboard=True)
    row = [KeyboardButton(x) for x in numbers]
    markup.add(*row)

    return markup


@bot.message_handler(commands=['low'])
def survey(message: Message) -> None:
    bot.send_message(message.from_user.id, f'В каком городе будет проводиться поиск?.',
                                           reply_markup=ReplyKeyboardRemove())

    bot.set_state(message.from_user.id, SearchInfoState.city, message.chat.id)


@bot.message_handler(state=SearchInfoState.city)
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
        bot.send_message(message.from_user.id, 'Сколько отелей вывести? (от 1 до 10)', reply_markup=keyboard(keys))
        bot.set_state(message.from_user.id, SearchInfoState.hotels_quantity, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['city'] = message.text.title()
    else:
        bot.send_message(message.from_user.id, 'Город может содержать только буквы.')


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
        bot.send_message(message.from_user.id, 'Введите количество отелей (от 1 до 10).', reply_markup=keyboard(keys))


@bot.message_handler(state=SearchInfoState.confirm_photo)
def get_confirm_photo(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['confirm_photo'] = message.text
    if message.text.title() == 'Да':
        bot.send_message(message.from_user.id, 'Сколько фотографий вывести? (от 1 до 10)', reply_markup=keyboard(keys))
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
                         reply_markup=keyboard(keys))

