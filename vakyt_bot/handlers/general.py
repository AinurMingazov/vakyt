from aiogram import Router
from aiogram.types import Message
from aiogram.utils.markdown import hbold




from aiogram.filters.command import Command


general_router = Router()


@general_router.message(Command('start'))
async def command_start(message: Message): ...


@general_router.message(Command('start_timer'))
async def command_start_timer(message: Message): ...


@general_router.message(Command('stop_timer'))
async def command_stop_timer(message: Message): ...


@general_router.message(Command('reminder'))
async def command_reminder(message: Message): ...


@general_router.message(Command('help'))
async def command_help(message: Message) -> None:
    await message.answer(f'👋 Добрый день, {hbold(message.from_user.full_name)}!')
