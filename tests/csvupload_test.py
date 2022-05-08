# This test checks if the transactions csv file exists within the upload folder:
def test_csvupload(client):
    file = "./app/uploads/transactions-new.csv"
    data = {'file': (open(file, 'rb'), file)}
    res = client.get("/login")
    assert res.status_code == 200
