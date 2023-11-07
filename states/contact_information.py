from telebot.handler_backends import State, StatesGroup


class SearchInfoState(StatesGroup):
    country = State()
    city = State()
    hotels_quant = State()
    photo_quant = State()
    confirm_photo = State()


class UserInfoState(StatesGroup):
    name = State()
    age = State()
    country = State()
    city = State()
    phone_number = State()
