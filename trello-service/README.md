# Trello Service

Этот микросервис управляет карточками Trello.

## 🚀 Запуск сервиса

1. Установите зависимости:
pip install -r requirements.txt

markdown
Копировать
Редактировать

2. Запустите сервер:
uvicorn app:app --reload --host 0.0.0.0 --port 8000

markdown
Копировать
Редактировать

## 📌 API эндпоинты

- `POST /trello/create_card` - Создать карточку.
- `PUT /trello/update_card` - Изменить карточку.
