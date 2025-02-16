import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from config import config, logger
from bot_handlers import routers

# Логируем запуск бота
logger.info("🚀 Telegram Bot запускается...")

# Создаём бота и диспетчер
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

# Регистрируем обработчики из bot_handlers
for router in routers:
    dp.include_router(router)

# Создаём новый router для автоудаления сообщений
auto_delete_router = Router()
dp.include_router(auto_delete_router)  # Регистрируем этот router

# Глобальные переменные для хранения сообщений
user_messages = {}  # Список сообщений пользователя
last_activity = {}  # Время последнего взаимодействия

async def delete_all_messages(user_id: int, bot: Bot):
    """Удаляет все сообщения пользователя, если он был неактивен 30 минут."""
    if user_id in user_messages:
        for msg_id in user_messages[user_id]:
            try:
                await bot.delete_message(chat_id=user_id, message_id=msg_id)
            except Exception:
                pass  # Пропускаем ошибки, если сообщение уже удалено
        user_messages[user_id] = []  # Очищаем список
        logger.info(f"🗑️ Все сообщения пользователя {user_id} удалены из чата.")

async def schedule_message_cleanup(user_id: int, bot: Bot):
    """Запускает таймер на 30 минут и удаляет сообщения, если пользователь неактивен."""
    await asyncio.sleep(1800)  # Ждём 30 минут (1800 секунд)
    now = datetime.now()
    
    if user_id in last_activity and (now - last_activity[user_id]).seconds >= 1800:
        await delete_all_messages(user_id, bot)  # Удаляем все сообщения

@auto_delete_router.message()
async def handle_message(message: types.Message):
    """Обрабатывает сообщения, сохраняет их и обновляет таймер."""
    user_id = message.from_user.id
    now = datetime.now()

    # Сохраняем ID сообщений, отправленных ботом
    if user_id not in user_messages:
        user_messages[user_id] = []
    
    # Отправляем новое сообщение
    sent_message = await message.answer("Ваше новое сообщение...")

    # Сохраняем ID ответа бота (чтобы не удалять сообщения пользователя)
    user_messages[user_id].append(sent_message.message_id)

    # Обновляем время последнего взаимодействия
    last_activity[user_id] = now

    # Запускаем таймер удаления (но только один раз)
    if len(user_messages[user_id]) == 1:  
        asyncio.create_task(schedule_message_cleanup(user_id, message.bot))

async def main():
    """Запуск бота"""
    logger.info("✅ Telegram Bot успешно запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())  # Запускаем asyncio loop правильно
    except Exception as e:
        logger.error(f"❌ Ошибка в работе бота: {e}")



