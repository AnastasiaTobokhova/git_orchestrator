import pytest
from aiogram.types import Message, CallbackQuery
from bot_handlers.start_handler import start_command
from bot_handlers.commands_handler import help_command, info_command
from bot_handlers.github_handler import get_github_repos, create_github_repo, receive_repo_name
from bot_handlers.jenkins_handler import jenkins_build, jenkins_status, jenkins_logs
from bot_handlers.trello_handler import trello_create_card, receive_card_name, trello_update_card

# 📌 Тест команды /start
@pytest.mark.asyncio
async def test_start_command():
    message = Message(message_id=1, chat={"id": 123}, text="/start")
    response = await start_command(message)
    assert response.text == "Привет! Я твой Telegram-бот. Чем могу помочь?"

# 📌 Тест команды /help
@pytest.mark.asyncio
async def test_help_command():
    message = Message(message_id=2, chat={"id": 123}, text="/help")
    response = await help_command(message)
    assert "Вот список доступных команд" in response.text

# 📌 Тест команды /info
@pytest.mark.asyncio
async def test_info_command():
    message = Message(message_id=3, chat={"id": 123}, text="/info")
    response = await info_command(message)
    assert "Этот бот взаимодействует с API сервисами GitHub, Jenkins и Trello." in response.text

# 📌 Тест команды /github_repos (список репозиториев)
@pytest.mark.asyncio
async def test_get_github_repos(mocker):
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=200, json=lambda: [{"name": "repo1"}, {"name": "repo2"}]))

    message = Message(message_id=4, chat={"id": 123}, text="/github_repos")
    response = await get_github_repos(message)
    assert "Выберите репозиторий:" in response.text

# 📌 Тест создания репозитория (GitHub)
@pytest.mark.asyncio
async def test_create_github_repo(mocker):
    mocker.patch("requests.post", return_value=mocker.Mock(status_code=201))

    message = Message(message_id=5, chat={"id": 123}, text="test-repo")
    response = await receive_repo_name(message)
    assert "✅ Репозиторий 'test-repo' успешно создан!" in response.text



# 📌 Тест команды /trello_create_card (создание карточки Trello)
@pytest.mark.asyncio
async def test_trello_create_card(mocker):
    mocker.patch("requests.post", return_value=mocker.Mock(status_code=201))

    message = Message(message_id=9, chat={"id": 123}, text="New Trello Card")
    response = await receive_card_name(message)
    assert "✅ Карточка **New Trello Card** создана!" in response.text

# 📌 Тест команды /trello_update_card (обновление карточки Trello)
@pytest.mark.asyncio
async def test_trello_update_card(mocker):
    mocker.patch("requests.put", return_value=mocker.Mock(status_code=200))

    message = Message(message_id=10, chat={"id": 123}, text="card123 done")
    response = await trello_update_card(message)
    assert "✅ Карточка card123 обновлена" in response.text

