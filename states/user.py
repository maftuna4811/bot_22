from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    chat_id = State()
    full_name = State()
    phone_number = State()
    location = State()