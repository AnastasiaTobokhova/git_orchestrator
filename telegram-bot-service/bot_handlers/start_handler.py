from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import logger

router = Router()

# 🔹 Функция создания inline-клавиатуры главного меню
def main_menu_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="📂 GitHub: Репозитории", callback_data="github_repos")
    keyboard.button(text="🚀 GitHub Actions: Запуск CI/CD", callback_data="ci_cd_start")
    keyboard.button(text="📊 GitHub Actions: Статус сборки", callback_data="ci_cd_status")
    keyboard.button(text="📝 GitHub Actions: Логи сборки", callback_data="ci_cd_logs")
    keyboard.button(text="🏁 Trello: Создать карточку", callback_data="trello_create_card")
    keyboard.button(text="🔄 Trello: Обновить карточку", callback_data="trello_update_card")
    keyboard.adjust(1)
    return keyboard.as_markup()

# 🔹 Обработчик команды /start
@router.message(CommandStart())
async def start_command(message: types.Message):
    logger.info(f"🔹 Пользователь {message.from_user.id} отправил команду /start")
    await message.answer("👋 Привет! Выбери действие ниже:", reply_markup=main_menu_keyboard())

    

