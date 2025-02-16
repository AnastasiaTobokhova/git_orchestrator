# 🚀 GitHub Actions Telegram Bot

Этот проект — **микросервисный Telegram-бот** для работы с **GitHub Actions, Trello и CI/CD**.

## 📌 Функции:
✅ Запуск GitHub Actions  
✅ Получение статуса и логов CI/CD  
✅ Создание и обновление карточек Trello  
✅ Взаимодействие через **интуитивный Telegram-интерфейс**

---

## 🛠 **Стек технологий**
- **Python (Aiogram, FastAPI)**
- **Docker & Docker Compose**
- **GitHub Actions**
- **PostgreSQL**
- **Trello API**
- **Telegram Bot API**

---

## 📦 **Установка и запуск**
1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/AnastasiaTobokhova/git_orchestrator.git
   cd git_orchestrator

2. **Создайте .env файл и добавьте секреты:**

TELEGRAM_BOT_TOKEN=your_token
GITHUB_TOKEN=your_github_token
TRELLO_API_KEY=your_trello_api_key
TRELLO_TOKEN=your_trello_token
Запустите сервисы через Docker:

```bash
   docker-compose up --build
   
Запустите бота вручную (если без Docker):

3. **Запустите сервисы через Docker:**
```bash 
   cd telegram-bot-service
   python main.py

## 🤖 Как пользоваться

1️⃣ Напишите /start боту в Telegram
2️⃣ Выберите нужное действие (например, "Запуск CI/CD")
3️⃣ Следите за процессом в реальном времени


## 🏗 Развитие проекта
🔹 Подключить Kubernetes
🔹 Добавить автоматический деплой
🔹 Улучшить логи и мониторинг

## 📩 Контакты
Если у вас есть вопросы, пишите мне:
📬 Telegram: @anastasssssssia
📧 Email: anastasia.tobohova@yandex.ru


## ✨ Лицензия
MIT License. Подробнее в файле `LICENSE`.
=======