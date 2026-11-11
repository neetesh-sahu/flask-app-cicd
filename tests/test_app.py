from app import create_app

def setup_function():
    global client

    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert b"Flask CI/CD Pipeline is Running!" in response.data


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_api_info():
    response = client.get("/api/info")

    assert response.status_code == 200
    assert response.json["project"] == "Flask Docker CI/CD"