import json


def test_create_job(client):
    payload = {
        "title": "some job",
        "company": "co.inc",
        "company_url": "http://some.url.net",
        "description": "some text job",
        "location": "nowhere",
        "date_posted": "2023-01-08",
        "is_active": True
    }
    response = client.post('/jobs/', data=json.dumps(payload))
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "some job"
    assert data["description"] == "some text job"
    assert data["is_active"] == True


def test_read_job(client):
    payload = {
        "title": "SDE super",
        "company": "not hehe",
        "company_url": "http://not.hehe.net",
        "location": "USA, NY",
        "description": "python",
        "date_posted": "2023-01-08",
    }
    client.post('/jobs/', data=json.dumps(payload))
    response = client.get('/jobs/1/')
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "SDE super"
