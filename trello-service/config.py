import os
import logging
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Настройки логирования
LOG_FILE = "logs/bot.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),  # Лог в файл
        logging.StreamHandler()  # Лог в консоль
    ]
)

logger = logging.getLogger(__name__)

class Config:
    TRELLO_API_URL = "https://api.trello.com/1"
    TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
    TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
    TRELLO_BOARD_ID = os.getenv("TRELLO_BOARD_ID")

config = Config()
