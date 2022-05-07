def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/")
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200