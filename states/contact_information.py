from telebot.handler_backends import State, StatesGroup


class SearchInfoState(StatesGroup):
    country = State()
    city = State()
    hotels_quantity = State()
    photo_quantity = State()
    confirm_photo = State()
