import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import patch
from src.routers.challenges import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


@pytest.fixture(autouse=True)
def mock_service_methods():
    with patch("src.services.challenges_service.virus_propagation") as vp, \
            patch("src.services.challenges_service.count_end89") as ce, \
            patch("src.services.challenges_service.recycling") as rc:
        vp.return_value = 89
        ce.return_value = 34
        rc.return_value = 4
        yield vp, ce, rc


def test_solution_1_returns_propagation_value(mock_service_methods):
    n = 10
    response = client.get(f"/challenges/solution-1?n={n}")
    assert response.status_code == 200
    assert response.text.strip('"') == str(89)
    vp, _, _ = mock_service_methods
    vp.assert_called_once_with(n)


def test_solution_2_returns_count_value(mock_service_methods):
    n = 44
    response = client.get(f"/challenges/solution-2?n={n}")
    assert response.status_code == 200
    assert response.text.strip('"') == str(34)
    _, ce, _ = mock_service_methods
    ce.assert_called_once_with(n)


def test_solution_3_returns_recycling_result(mock_service_methods):
    matrix_data = [
        [2, 0, 1],
        [0, 3, 1],
        [1, 1, 1]
    ]
    response = client.post("/challenges/solution-3", json=matrix_data)
    assert response.status_code == 200
    assert response.text.strip('"') == str(4)
    _, _, rc = mock_service_methods
    rc.assert_called_once_with(matrix_data)
