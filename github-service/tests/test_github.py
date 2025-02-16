import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# 🔢 Тест получения списка репозиториев
def test_get_repositories(mocker):
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=200, json=lambda: [{"name": "repo1"}]))
    response = client.get("/github/repositories")
    assert response.status_code == 200
    assert response.json() == [{"name": "repo1"}]

# ➕ Тест создания репозитория
def test_create_repository(mocker):
    mocker.patch("requests.post", return_value=mocker.Mock(status_code=201, json=lambda: {"name": "new_repo"}))
    response = client.post("/github/create_repo", json={"repo_name": "new_repo"})
    assert response.status_code == 200
    assert response.json()["repo"]["name"] == "new_repo"

# ✉️ Тест создания задачи (issue)
def test_create_issue(mocker):
    mocker.patch("requests.post", return_value=mocker.Mock(status_code=201, json=lambda: {"title": "Bug"}))
    response = client.post("/github/create_issue", json={"repo": "repo1", "title": "Bug"})
    assert response.status_code == 200
    assert response.json()["issue"]["title"] == "Bug"
