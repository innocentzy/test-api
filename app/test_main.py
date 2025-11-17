from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_get_questions():
    response = client.get("/questions")
    assert response.status_code == 200