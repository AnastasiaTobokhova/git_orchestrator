import logging
from aiogram import Router, types
from config import logger

router = Router()

@router.errors()
async def error_handler(event: types.ErrorEvent):
    logging.error(f"Ошибка: {event.exception}")
