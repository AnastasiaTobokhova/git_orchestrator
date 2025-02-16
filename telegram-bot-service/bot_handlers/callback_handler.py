from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from . import github_handler, ci_cd_handler, trello_handler
from config import logger

router = Router()

# 🔹 Обработчик нажатий на inline-кнопки
@router.callback_query(F.data)
async def callback_handler(callback: CallbackQuery):
    action = callback.data
    user_id = callback.from_user.id

    if action == "github_repos":
        logger.info(f"📂 Пользователь {user_id} запросил список репозиториев")
        await github_handler.get_github_repos(callback.message)

    elif action.startswith("deploy_repo_"):
        repo_name = action.replace("deploy_repo_", "").strip()
        logger.info(f"🚀 Пользователь {user_id} выбрал репозиторий {repo_name} для деплоя")
        await ci_cd_handler.trigger_github_actions(callback.message, repo_name=repo_name)
        await callback.answer(f"🚀 Запуск GitHub Actions для {repo_name}...")

    elif action == "ci_cd_status":
        logger.info(f"📊 Пользователь {user_id} запросил статус сборки")
        await ci_cd_handler.github_actions_status(callback.message)

    elif action == "ci_cd_logs":
        logger.info(f"📝 Пользователь {user_id} запросил логи сборки")
        await ci_cd_handler.github_actions_logs(callback.message)

    elif action == "trello_create_card":
        logger.info(f"🏁 Пользователь {user_id} создаёт карточку Trello")
        await trello_handler.trello_create_card(callback.message, repo_name="unknown", build_status="pending")

    elif action == "trello_update_card":
        logger.info(f"🔄 Пользователь {user_id} обновляет карточку Trello")
        await trello_handler.trello_update_card(callback.message)

    await callback.answer()







