# This test checks if the music csv file exists within the upload folder:
def test_csvupload(client):
    file = "./app/uploads/transactions-new.csv"
    data = {'file': (open(file, 'rb'), file)}

    # once the login test works I copy that code here for logging in
    res = client.get("/login")
    assert res.status_code == 200
