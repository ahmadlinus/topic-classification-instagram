from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_entry_api():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello World!"


def test_topic_classification():
    sample_data = {"text": "How are you?"}
    headers = {"Content-Type": "application/json"}
    response = client.post("/topics", json=sample_data, headers=headers)
    assert response.status_code == 200
    assert len(response.json()) > 1