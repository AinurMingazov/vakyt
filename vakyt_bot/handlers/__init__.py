from aiogram.filters.callback_data import CallbackData


class CustomCallback(CallbackData, prefix='custom'):
    action: str
