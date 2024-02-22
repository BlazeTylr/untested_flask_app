import json

def test_getting_data(web_client):
    get_response = web_client.get('/users')
    assert get_response.status_code == 200
    assert json.loads(get_response.data.decode('utf-8')) == [
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

def test_get_user_not_found(web_client):
    response = web_client.get("/users/4")
    assert response.status_code == 404
    assert  json.loads(response.data.decode('utf-8')) == {'error': 'User not found'}