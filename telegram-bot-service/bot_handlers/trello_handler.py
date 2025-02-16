from aiogram import Router, types, F
from aiogram.filters import Command
import requests
from config import config, logger
import os

router = Router()

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
TRELLO_BOARD_ID = os.getenv("TRELLO_BOARD_ID")

# 🏁 Создание карточек задач
@router.message(F.text == "/trello_create_card")
async def trello_create_card(message: types.Message, repo_name: str, build_status: str):
    url = "https://api.trello.com/1/cards"
    params = {
        "name": f"Deploy {repo_name}",
        "desc": f"Статус: {build_status}",
        "idList": TRELLO_BOARD_ID,
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN
    }
    response = requests.post(url, params=params)

    if response.status_code == 200:
        await message.answer(f"✅ Карточка Trello успешно создана для {repo_name}!")
    else:
        logger.error(f"Ошибка создания карточки Trello: {response.json()}")
        await message.answer("❌ Ошибка создания карточки Trello.")

# 🔄 Изменение статусов карточек
@router.message(F.text == "/trello_update_card")
async def trello_update_card(message: types.Message):
    await message.answer("Введите ID карточки и новый статус (через пробел):")

@router.message(F.text)
async def receive_card_status_update(message: types.Message):
    data = message.text.split()
    if len(data) < 2:
        await message.answer("❌ Неверный формат. Введите ID карточки и новый статус через пробел.")
        return

    card_id, new_status = data[0], data[1]
    response = requests.put(f"{config.TRELLO_API_URL}/update_card", json={"id": card_id, "status": new_status})
    if response.status_code == 200:
        logger.info(f"📌 Обновление карточки Trello {card_id} от {message.from_user.id}")
        await message.answer(f"✅ Карточка {card_id} обновлена до статуса **{new_status}**.")
    else:
        logger.error(f"❌ Ошибка при обновлении карточки: {response.text}")
        await message.answer("❌ Ошибка обновления карточки.")

