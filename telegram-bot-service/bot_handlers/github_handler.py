from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
import requests
from config import config, logger
import os

router = Router()

# 🔹 Определяем состояния FSM
class RepoCreation(StatesGroup):
    waiting_for_name = State()  # Ожидание ввода имени репозитория

class IssueCreation(StatesGroup):
    waiting_for_repo = State()  # Ожидание ввода имени репозитория
    waiting_for_title = State()  # Ожидание ввода заголовка задачи

class RepoAnalytics(StatesGroup):
    waiting_for_repo = State()  # Ожидание ввода имени репозитория

class PullRequests(StatesGroup):
    waiting_for_repo = State()  # Ожидание ввода имени репозитория

router = Router()

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
HEADERS = {
    "Authorization": f"token {config.GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# получение списка репозиториев
@router.message(F.text == "/github_repos")
async def get_github_repos(message: types.Message):
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get("https://api.github.com/user/repos", headers=headers)

    if response.status_code == 200:
        repos = response.json()
        if not repos:
            await message.answer("❌ У вас нет доступных репозиториев.")
            return

        keyboard = InlineKeyboardBuilder()
        for repo in repos:
            repo_name = repo["name"]
            keyboard.button(text=f"📂 {repo_name}", callback_data=f"deploy_repo_{repo_name}")

        keyboard.adjust(1)  # Располагаем кнопки в 1 колонку
        await message.answer("📂 Выберите репозиторий для деплоя:", reply_markup=keyboard.as_markup())
    else:
        logger.error(f"Ошибка получения репозиториев: {response.status_code}")
        await message.answer("❌ Ошибка получения списка репозиториев.")


@router.message(F.text == "/deploy")
async def trigger_github_actions(message: types.Message):
    repo_name = "AnastasiaTobokhova/test_deploy" 
    image_name = "test_deploy"

    url = f"{GITHUB_API_URL}/repos/{repo_name}/dispatches"
    headers = {
        "Accept": "application/vnd.github.everest-preview+json",
        "Authorization": f"token {config.GITHUB_TOKEN}"
    }
    payload = {
        "event_type": "deploy",
        "client_payload": {
            "image_name": image_name
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 204:
        logger.info(f"🚀 Деплой GitHub Actions запущен для {repo_name}")
        await message.answer(f"✅ Деплой запущен для `{repo_name}`!")
    else:
        logger.error(f"❌ Ошибка запуска GitHub Actions: {response.text}")
        await message.answer(f"❌ Ошибка запуска GitHub Actions.")

