from keyboards.reply.contact import request_contact
from loader import bot
from states.contact_information import SearchInfoState
from telebot.types import Message


@bot.message_handler(commands=['lowprice'])
def survey(message: Message) -> None:
    bot.set_state(message.from_user.id, SearchInfoState.city, message.chat.id)
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! '
                                           f'В каком городе будет проводиться поиск?.')


@bot.message_handler(state=SearchInfoState.city)
def get_city(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.from_user.id, 'Сколько отелей вывести? (от 1 до 10)')
        bot.set_state(message.from_user.id, SearchInfoState.hotels_quant, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['city'] = message.text.title()
    else:
        bot.send_message(message.from_user.id, 'Город может содержать только буквы.')


@bot.message_handler(state=SearchInfoState.hotels_quant)
def get_quantity(message: Message) -> None:
    if message.text.isdigit() and 0 < int(message.text) < 11:
        bot.send_message(message.from_user.id, 'Вывести фотографии? Да/Нет')
        bot.set_state(message.from_user.id, SearchInfoState.confirm_photo, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['hotels_quant'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Введите количество отелей (от 1 до 10).')


@bot.message_handler(state=SearchInfoState.confirm_photo)
def get_confirm_photo(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['confirm_photo'] = message.text
    if message.text.title() == 'Да':
        bot.send_message(message.from_user.id, 'Сколько фотографий вывести? (от 1 до 10)')
        bot.set_state(message.from_user.id, SearchInfoState.photo_quant, message.chat.id)

    else:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['photo_quant'] = 0
        text = f'Спасибо за предоставленную информацию. Ваши данные:\n' \
               f'Город: {data["city"]}\n' \
               f'Кол-во отелей: {data["hotels_quant"]}\n' \
               f'Вывод фото: {data["confirm_photo"]}\n' \
               f'Кол-во фото: {data["photo_quant"]}\n'
        bot.send_message(message.from_user.id, text)


@bot.message_handler(state=SearchInfoState.photo_quant)
def get_photo_quant(message: Message) -> None:
    if message.text.isdigit() and 0 < int(message.text) < 11:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['photo_quant'] = message.text

            text = f'Спасибо за предоставленную информацию. Ваши данные:\n' \
                   f'Город: {data["city"]}\n' \
                   f'Кол-во отелей: {data["hotels_quant"]}\n' \
                   f'Вывод фото: {data["confirm_photo"]}\n' \
                   f'Кол-во фото: {data["photo_quant"]}\n'
            bot.send_message(message.from_user.id, text)
    else:
        bot.send_message(message.from_user.id, 'Введите количество фотографий (от 1 до 10).')


