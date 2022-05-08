#def test_auth_pages(client):
    # Register the user in the database with credentials
# client.get("/register")
# response = client.post("/register", data = {
# "email": "test@mail",
        #"password": "testpassword"
# })

# assert b"Redirecting..." in response.data
    # Verify that we are redirecting to the login (since we just registered):
# assert b'href="/login"' in response.data
# assert response.status_code == 302

    # POST to the login with the email and password to authenticate
    #response = client.post("/login", data = {
#  "email": "test@mail",
#  "password": "testerpassword"
# })
#  assert b"Redirecting..." in response.data
    # Verify that we are redirecting to the dashboard
#   assert b'href="/dashboard"' in response.data
#   assert response.status_code == 302