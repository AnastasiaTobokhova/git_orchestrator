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
    GITHUB_API_URL = "https://api.github.com"
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

config = Config()
