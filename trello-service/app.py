from fastapi import FastAPI
from api.trello_api import router
from config import logger

app = FastAPI(title="Trello Service", description="API для работы с Trello")

# Подключаем маршруты
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logger.info("✅ Trello Service успешно запущен!")


@app.get("/")
async def root():
    return {"message": "Trello Service is running"}
