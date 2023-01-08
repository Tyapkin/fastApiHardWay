import json


def test_create_user(client):
    payload = {
        "username": "testuser",
        "email": "testuser@ema.il",
        "password": "testpswd"
    }
    response = client.post("/users/", data=json.dumps(payload))
    data = response.json()
    assert response.status_code == 200
    assert data["email"] == "testuser@ema.il"
    assert data["is_active"] == True
