from app.db.models import User


def test_auth_pages(client):
    # client.get("/")
    # client.get("/logout")
    #
    # Register the user in the database with credentials
    # client.get("/register")
    # response = client.post("/register", data={
    #     "email": "test@mail",
    #     "password": "testpassword"
    # })
    #
    # assert b"Redirecting..." in response.data
    # # Verify that we are redirecting to the login (since we just registered):
    # assert b'href="/login"' in response.data
    # assert response.status_code == 302


    # Check the database to make sure the new user has been registered (created):
    #user = User.query.filter_by(email='test@mail').first()
    #assert user.email == "test@mail"



    #
    # POST to the login with the email and password to authenticate
    response = client.post("/login", data={
        "email": "test@mail",
        "password": "testerpassword"
    })
    #
    #
    assert b"Redirecting..." in response.data
    # # Verify that we are redirecting to the dashboard
    assert b'href="/login"' in response.data
    assert response.status_code == 302
