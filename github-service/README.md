# GitHub Service

Этот микросервис работает с GitHub API.

## 🚀 Запуск сервиса

1. Установите зависимости:
pip install -r requirements.txt


2. Запустите сервер:
uvicorn app:app --reload --host 0.0.0.0 --port 8000


## 📌 API эндпоинты

- `GET /github/repositories` - Получить список репозиториев.
- `POST /github/create_repo` - Создать новый репозиторий.
- `POST /github/create_issue` - Создать задачу (issue).
- `GET /github/repo_analytics/{repo}` - Получить аналитику репозитория.
- `GET /github/pull_requests/{repo}` - Получить список Pull Requests.
