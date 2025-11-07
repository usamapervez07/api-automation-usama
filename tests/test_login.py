from endpoints.login_api import login_user

def test_login():
    status_code = login_user("usama.pervez@emumba.com", "Usama1234!")
    assert status_code == 200