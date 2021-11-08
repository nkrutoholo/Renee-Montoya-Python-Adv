import pytest
from .conftest import client


def test_post(client):
    response = client.post("/api/v1/todos")

    assert response.status_code == 200


def test_get(client):
    response = client.get("/api/v1/todos")

    assert response.status_code == 200


# def test_patch(client):
#     response = client.patch("/api/v1/todos")
#
#     assert response.status_code == 200
#
#
# def test_delete(client):
#     response = client.delete("/api/v1/todos")
#
#     assert response.status_code == 200
