import requests

from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello YOLO World"}