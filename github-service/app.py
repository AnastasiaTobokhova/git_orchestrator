from fastapi import FastAPI, HTTPException
from api.github_api import router
from config import logger

app = FastAPI(title="GitHub Service", description="API для работы с GitHub")

# Подключаем маршруты
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logger.info("✅ GitHub Service успешно запущен!")

@app.get("/")
async def root():
    return {"message": "GitHub Service is running"}


