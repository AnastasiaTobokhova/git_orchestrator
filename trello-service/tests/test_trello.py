import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# 🏁 Тест создания карточки
def test_create_card(mocker):
    mocker.patch("requests.post", return_value=mocker.Mock(status_code=200, json=lambda: {"name": "Test Card"}))
    response = client.post("/trello/create_card", json={"name": "Test Card", "list_id": "list123"})
    assert response.status_code == 200
    assert response.json()["card"]["name"] == "Test Card"

# 🔄 Тест обновления карточки
def test_update_card(mocker):
    mocker.patch("requests.put", return_value=mocker.Mock(status_code=200, json=lambda: {"id": "card123"}))
    response = client.put("/trello/update_card", json={"card_id": "card123", "list_id": "list456"})
    assert response.status_code == 200
    assert response.json()["card"]["id"] == "card123"
