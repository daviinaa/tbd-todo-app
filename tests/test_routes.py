import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_add_task(client):
    response = client.post("/add", json={"task": "Test Task"})
    assert response.status_code == 201
    assert response.json["task"] == "Test Task"
