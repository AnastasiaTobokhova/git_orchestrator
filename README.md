# 🚀 CI/CD Telegram Bot

Этот проект представляет собой **Telegram-бота**, который интегрируется с **GitHub Actions** и **Trello**, позволяя пользователю:
- Просматривать список своих репозиториев на GitHub.
- Запускать CI/CD пайплайн через **GitHub Actions**.
- Отслеживать статус и логи выполнения пайплайна.
- Создавать и обновлять карточки **Trello**.

---

## 📌 Функционал

🔹 **GitHub**
- Просмотр списка репозиториев.
- Запуск **GitHub Actions** для CI/CD.
- Получение статуса и логов сборки.

🔹 **Trello**
- Создание карточек с информацией о билде.
- Обновление статуса карточек.

---

## 🛠️ Установка и запуск

### 1️⃣ Клонирование репозитория
```sh
 git clone https://github.com/AnastasiaTobokhova/git_orchestrator.git
 cd git_orchestrator
```

### 2️⃣ Настройка переменных окружения
Создайте файл `.env` в корневой папке и добавьте:
```
BOT_TOKEN=твой_токен_бота
GITHUB_TOKEN=твой_токен_гитхаба
TRELLO_API_KEY=твой_api_ключ_trello
TRELLO_TOKEN=твой_токен_trello
```

### 3️⃣ Запуск через Docker Compose
```sh
docker-compose up --build
```

---

## 🔗 Интеграция с GitHub Actions

Файл workflow находится в:
```
.github/workflows/ci_cd.yml
```
Для запуска CI/CD **бот отправляет запрос** в этот workflow через GitHub API.

### Пример workflow (ci_cd.yml)
```yaml
name: CI/CD Pipeline

on:
  repository_dispatch:
    types: [deploy]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: 🔹 Checkout репозитория
        uses: actions/checkout@v4

      - name: 🔹 Установка Docker
        run: |
          sudo apt-get update
          sudo apt-get install -y docker.io

      - name: 🔹 Билд и пуш Docker-образа
        run: |
          docker build -t ${{ secrets.REGISTRY_ID }}/image_name:latest .
          docker push ${{ secrets.REGISTRY_ID }}/image_name:latest
```

---

## 🔧 Основные технологии
- **Python** (aiogram, requests)
- **GitHub API** (вызов Actions, получение логов)
- **Trello API** (создание и обновление карточек)
- **Docker & Docker Compose** (контейнеризация)
- **GitHub Actions** (CI/CD пайплайн)

---

## 📌 TODO / Возможные улучшения
- [ ] Добавить поддержку Kubernetes.
- [ ] Улучшить обработку ошибок и логирование.
- [ ] Сделать интерфейс бота более интерактивным.

---

## 🤝 Контакты
📧 Email: anastasia.tobohova@yandex.ru

_Если у тебя есть идеи или вопросы – пиши, буду рада сотрудничеству!_ 😊



## ✨ Лицензия
MIT License. Подробнее в файле `LICENSE`.
=======
