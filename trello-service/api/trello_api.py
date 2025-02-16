import requests
from fastapi import APIRouter, HTTPException
from config import config,logger

router = APIRouter(prefix="/trello", tags=["Trello"])

TRELLO_AUTH = f"key={config.TRELLO_API_KEY}&token={config.TRELLO_TOKEN}"

# 🏁 Создание карточек задач
@router.post("/create_card")
async def create_card(name: str, list_id: str):
    url = f"{config.TRELLO_API_URL}/cards?{TRELLO_AUTH}"
    data = {
        "name": name,
        "idList": list_id
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        logger.info("✅ Успешно создана карточка - trello")
        return {"message": "Карточка создана!", "card": response.json()}
    logger.error(f"❌ Ошибка создания карточки - trello: {response.json()}")
    raise HTTPException(status_code=response.status_code, detail=response.json())

# 🔄 Изменение статусов карточек
@router.put("/update_card")
async def update_card(card_id: str, list_id: str):
    url = f"{config.TRELLO_API_URL}/cards/{card_id}?{TRELLO_AUTH}"
    data = {"idList": list_id}
    response = requests.put(url, json=data)

    if response.status_code == 200:
        logger.info("✅ Успешно изменени статус - trello")
        return {"message": "Карточка обновлена!", "card": response.json()}
    logger.error(f"❌ Ошибка изменения статуса - trello: {response.json()}")
    raise HTTPException(status_code=response.status_code, detail=response.json())
