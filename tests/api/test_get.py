import requests
from pages.login_page import LoginPage
def test_get_user(users_api):
    response = users_api.get_user(2)

    assert response.status_code == 200

    body = response.json()
    assert body["data"]["id"] == 2
    assert body["data"]["email"] == "janet.weaver@reqres.in"