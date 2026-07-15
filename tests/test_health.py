from fastapi.testclient import TestClient

from app.main import app


def test_health_endpoint_runs_without_optional_credentials() -> None:
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "application": "Tri9T AI CT-200 Backend",
        "environment": "development",
    }
