import unittest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

class UtilTest(unittest.TestCase):
    def test_index(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"url": "/docs", "message": "pour visualiser l'interface SwaggerUI"}