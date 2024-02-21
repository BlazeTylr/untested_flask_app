import json

def test_getting_data(web_client):
    post_response = web_client.get('/users')
    assert post_response.status_code == 200
    assert json.loads(post_response.data.decode('utf-8')) == [
    {
        "id": 1,
        "username": "john"
    },
    {
        "id": 2,
        "username": "jane"
    },
    {
        "id": 3,
        "username": "alice"
    }]

def test_example(web_client):
    response = web_client.get("/users")
    assert response.status_code == 200
    assert len(response.json) == 3