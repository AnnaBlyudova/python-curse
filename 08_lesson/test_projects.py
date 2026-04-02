import requests
import uuid
import pytest
import os

base_url = "https://ru.yougile.com/api-v2/"

# Токен берется из переменной окружения YOUGILE_TOKEN
TOKEN = os.getenv("YOUGILE_TOKEN")
if not TOKEN:
    pytest.skip("Нет токена. Установи переменную окружения YOUGILE_TOKEN", allow_module_level=True)


def create_project(title):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"title": title}
    resp = requests.post(base_url + 'projects', headers=headers, json=payload)
    return resp


def update_project(project_id, new_title):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"title": new_title}
    resp = requests.put(f"{base_url}projects/{project_id}", headers=headers, json=payload)
    return resp


def get_project(project_id):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    resp = requests.get(f"{base_url}projects/{project_id}", headers=headers)
    return resp


def delete_project(project_id):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    resp = requests.delete(f"{base_url}projects/{project_id}", headers=headers)
    return resp


def test_create_project_positive():
    title = f"Тест {uuid.uuid4().hex[:6]}"
    response = create_project(title)

    assert response.status_code == 201
    body = response.json()
    assert "id" in body

    project_id = body["id"]
    get_response = get_project(project_id)
    assert get_response.status_code == 200
    assert get_response.json()["title"] == title

    delete_project(project_id)


def test_create_project_negative_empty_title():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(base_url + 'projects', headers=headers, json={"title": ""})

    assert response.status_code == 400
    body = response.json()
    assert "error" in body or "message" in body


def test_update_project_positive():
    title = f"Для обновления {uuid.uuid4().hex[:6]}"
    create_response = create_project(title)
    assert create_response.status_code == 201
    project_id = create_response.json()["id"]

    new_title = f"Обновлено {uuid.uuid4().hex[:6]}"
    update_response = update_project(project_id, new_title)

    assert update_response.status_code == 200

    get_response = get_project(project_id)
    assert get_response.status_code == 200
    assert get_response.json()["title"] == new_title

    delete_project(project_id)


def test_update_project_negative_invalid_id():
    fake_id = "00000000-0000-0000-0000-000000000000"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.put(f"{base_url}projects/{fake_id}", headers=headers, json={"title": "Новое"})

    assert response.status_code == 404
    body = response.json()
    assert "error" in body or "message" in body


def test_get_project_positive():
    title = f"Для получения {uuid.uuid4().hex[:6]}"
    create_response = create_project(title)
    assert create_response.status_code == 201
    project_id = create_response.json()["id"]

    response = get_project(project_id)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == project_id
    assert body["title"] == title

    delete_project(project_id)


def test_get_project_negative_not_found():
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = get_project(fake_id)

    assert response.status_code == 404
    body = response.json()
    assert "error" in body or "message" in body
