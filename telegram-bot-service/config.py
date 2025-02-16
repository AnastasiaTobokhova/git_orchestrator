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
    # 🔹 Telegram Bot
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # 🔹 API URLs
    GITHUB_API_URL = os.getenv("GITHUB_API_URL", "http://github-service:8000")
    JENKINS_URL = os.getenv("JENKINS_API_URL", "http://jenkins-service:8080")
    TRELLO_API_URL = os.getenv("TRELLO_API_URL", "http://trello-service:8000")

    # 🔹 GitHub API
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

    # 🔹 Jenkins API
    JENKINS_USER = os.getenv("JENKINS_USER")
    JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")
    JENKINS_AUTH = os.getenv("JENKINS_AUTH")

    # 🔹 Trello API
    TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
    TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
    TRELLO_BOARD_ID = os.getenv("TRELLO_BOARD_ID")

    # 🔹 PostgreSQL Database (для Telegram-бота)
    DB_HOST = os.getenv("DB_HOST", "db")  # 'db', если в Docker; 'localhost', если локально
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "telegram_bot_db")
    DB_USER = os.getenv("DB_USER", "bot_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "bot_password")

    # Полный URL для SQLAlchemy
    DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

config = Config()

