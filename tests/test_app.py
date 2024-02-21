
def test_example(web_client):
    response = web_client.get("/users")
    assert response.status_code == 200
    assert len(response.json) == 3


