from fastapi.testclient import TestClient
from app import app
import json

client = TestClient(app.app)

def test_get():
    response = client.post(
            "/tabs/create",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"total": 42.99}))
    assert response.status_code == 201
    assert response.json()["tab_id"] == 1
    response = client.post(
            "/tabs/create",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"total": 42.99}))
    assert response.status_code == 201
    assert response.json()["tab_id"] == 2
    response = client.post("users/create")
    assert response.status_code == 201
    assert response.json()["user_id"] == 1
    response = client.post(
            "/items/create",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"tab_id": 1, "item_total": 42.99}))
    assert response.status_code == 201
    assert response.json()["item_id"] == 1
    response = client.post(
            "/items/add_user",
            data=json.dumps({"item_id": 1, "user_id": 1, "portion": 20}))
    assert response.status_code == 201
    response = client.get("/tabs/paid/1")
    assert response.status_code == 200
    assert response.json() == {"tab_total": 42.99, "tab_paid": 0}
    response = client.post(
            "/users/pay",
            data=json.dumps({"user_id": 1}))
    assert response.status_code == 200
    response = client.get(
            "/tabs/paid/1")
    assert response.status_code == 200
    assert response.json() == {"tab_total": 42.99, "tab_paid": 20}

    
