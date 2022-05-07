def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/login")
    assert response.status_code == 200
    # POST to the login with the email and password to authenticate
    response = client.post("/login", data = {
        "email": "test@test",
        "password": "testtest"
    })
    assert b"Redirecting..." in response.data
    # Verify that we are redirecting to the dashboard
    assert b'href="/dashboard"' in response.data
    assert response.status_code == 302