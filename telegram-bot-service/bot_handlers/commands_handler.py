from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Вот список доступных команд:\n/help - помощь\n/info - информация")

@router.message(Command("info"))
async def info_command(message: types.Message):
    await message.answer("Этот бот взаимодействует с API сервисами GitHub, Jenkins и Trello.")
