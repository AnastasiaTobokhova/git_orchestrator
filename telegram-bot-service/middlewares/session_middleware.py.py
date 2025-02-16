from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from database import get_db

class SessionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: TelegramObject, data: dict):
        async for session in get_db():
            data["db_session"] = session
            return await handler(event, data)

