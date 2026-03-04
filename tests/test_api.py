"""Tests for the Calculator API."""
import pytest
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)


class TestHealthCheck:
    def test_health(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"


class TestAddEndpoint:
    def test_add(self):
        response = client.post("/add", json={"a": 2, "b": 3})
        assert response.status_code == 200
        assert response.json()["result"] == 5
        assert response.json()["operation"] == "add"


class TestDivideEndpoint:
    def test_divide(self):
        response = client.post("/divide", json={"a": 10, "b": 2})
        assert response.status_code == 200
        assert response.json()["result"] == 5.0

    def test_divide_by_zero(self):
        response = client.post("/divide", json={"a": 10, "b": 0})
        assert response.status_code == 400


class TestPowerEndpoint:
    def test_power(self):
        response = client.post("/power", json={"a": 2, "b": 3})
        assert response.status_code == 200
        assert response.json()["result"] == 8

    def test_power_zero_negative(self):
        response = client.post("/power", json={"a": 0, "b": -1})
        assert response.status_code == 400
