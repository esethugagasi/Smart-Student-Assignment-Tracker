from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_assignments():

    response = client.get("/api/assignments")

    assert response.status_code == 200