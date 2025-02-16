import requests
from fastapi import APIRouter, HTTPException
from config import config,logger

router = APIRouter(prefix="/github", tags=["GitHub"])

HEADERS = {"Authorization": f"token {config.GITHUB_TOKEN}"}

# 🔢 Получение списка репозиториев
@router.get("/repositories")
async def get_repositories():
    url = f"{config.GITHUB_API_URL}/user/repos"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        logger.info("✅ Успешно получен список репозиториев")
        return response.json()
    logger.error(f"❌ Ошибка получения списка репозиториев: {response.json()}")
    raise HTTPException(status_code=response.status_code, detail=response.json())

# ➕ Создание нового репозитория
@router.post("/create_repo")
async def create_repository(repo_name: str):
    url = f"{config.GITHUB_API_URL}/user/repos"
    data = {"name": repo_name, "private": False}
    response = requests.post(url, json=data, headers=HEADERS)

    if response.status_code == 201:
        logger.info("✅ Успешно создан новый репозиторий")
        return {"message": "Репозиторий успешно создан", "repo": response.json()}
    logger.error(f"❌ Ошибка создания нового репозитория: {response.json()}")
    raise HTTPException(status_code=response.status_code, detail=response.json())

# ✉️ Создание задач (issues)
@router.post("/create_issue")
async def create_issue(repo: str, title: str, body: str = ""):
    url = f"{config.GITHUB_API_URL}/repos/YOUR_GITHUB_USERNAME/{repo}/issues"
    data = {"title": title, "body": body}
    response = requests.post(url, json=data, headers=HEADERS)

    if response.status_code == 201:
        logger.info("✅ Успешно создана задача")
        return {"message": "Issue создано", "issue": response.json()}
    logger.error(f"❌ Ошибка создания задачи: {response.json()}")
    raise HTTPException(status_code=response.status_code, detail=response.json())

# 🌟 Просмотр аналитики репозитория
@router.get("/repo_analytics/{repo}")
async def repo_analytics(repo: str):
    url = f"{config.GITHUB_API_URL}/repos/YOUR_GITHUB_USERNAME/{repo}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        logger.info("✅ Успешно создан запрос на просмотр аналитики")
        data = response.json()
        return {
            "stars": data["stargazers_count"],
            "forks": data["forks_count"],
            "views": "Данные по просмотрам недоступны в публичном API"
        }
    logger.error(f"❌ Ошибка создания запроса просмотра аналитики: {response.json()}")
    raise HTTPException(status_code=response.status_code, detail=response.json())

# 📝 Получение информации о Pull Requests
@router.get("/pull_requests/{repo}")
async def get_pull_requests(repo: str):
    url = f"{config.GITHUB_API_URL}/repos/YOUR_GITHUB_USERNAME/{repo}/pulls"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        logger.info("✅ Успешно получена информация о pull request")
        return response.json()
    logger.error(f"❌ Ошибка получения информации о pull request: {response.json()}")
    raise HTTPException(status_code=response.status_code, detail=response.json())
