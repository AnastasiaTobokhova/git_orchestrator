from aiogram import Router, types, F
import requests
import os
from config import config, logger
import aiohttp

router = Router()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USER = os.getenv("GITHUB_USER")
GITHUB_API_URL = "https://api.github.com"


# 🚀 Триггер GitHub Actions
@router.message(F.text == "/ci_cd_trigger")
async def trigger_github_actions(message: types.Message, repo_name: str):
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    workflow_url = f"https://api.github.com/repos/AnastasiaTobokhova/{repo_name}/actions/workflows/ci_cd.yml/dispatches"

    data = {"ref": "main"}
    response = requests.post(workflow_url, json=data, headers=headers)

    if response.status_code == 204:
        await message.answer(f"✅ GitHub Actions успешно запущен для {repo_name}!")
    else:
        logger.error(f"Ошибка запуска GitHub Actions: {response.json()}")
        await message.answer(f"❌ Ошибка запуска GitHub Actions.")

# 📊 Получение статуса GitHub Actions
@router.message(F.text == "/ci_cd_status")
async def github_actions_status(message: types.Message):
    await message.answer("Введите название репозитория:")

@router.message(F.text)
async def github_actions_status(message: types.Message):
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{GITHUB_API_URL}/repos/AnastasiaTobokhova/test_deploy/actions/runs",
            headers=headers
        ) as resp:
            if resp.status == 200:
                data = await resp.json()
                if data["workflow_runs"]:
                    last_run = data["workflow_runs"][0]
                    status = last_run["status"]
                    conclusion = last_run.get("conclusion", "в процессе")
                    await message.answer(f"📊 Статус последней сборки: **{status}**\n✅ Результат: **{conclusion}**")
                else:
                    await message.answer("⚠️ Нет запущенных workflow.")
            else:
                await message.answer("❌ Ошибка получения статуса.")

# 📝 Получение логов GitHub Actions
@router.message(F.text == "/ci_cd_logs")
async def github_actions_logs(message: types.Message):
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{GITHUB_API_URL}/repos/AnastasiaTobokhova/test_deploy/actions/runs",
            headers=headers
        ) as resp:
            if resp.status == 200:
                data = await resp.json()
                if data["workflow_runs"]:
                    last_run = data["workflow_runs"][0]
                    log_url = last_run["logs_url"]
                    await message.answer(f"📝 Логи последней сборки: [Скачать логи]({log_url})")
                else:
                    await message.answer("⚠️ Нет логов для отображения.")
            else:
                await message.answer("❌ Ошибка получения логов.")

