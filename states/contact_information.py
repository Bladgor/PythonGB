from telebot.handler_backends import State, StatesGroup


class SearchInfoState(StatesGroup):
    country = State()
    specify = State()
    city = State()
    hotels_quantity = State()
    photo_quantity = State()
    confirm_photo = State()
    check_city = State()
    command = State()


class Calendar(StatesGroup):
    check_in = State()
    check_out = State()
