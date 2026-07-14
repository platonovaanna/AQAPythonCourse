import requests

from clients import users_api
from pages.login_page import LoginPage
def test_create_user(users_api):
    payload = {"data": dict(email="test.weaver@reqres.in", first_name="test", last_name="test",
                            avatar="https://reqres.in/img/faces/2-image_update.jpg")}
    response = users_api.create_user(payload)
    assert response.status_code == 201
    body = response.json()
    assert body["data"]["email"] == "test.weaver@reqres.in"
    assert body["data"]["first_name"] == "test"
    assert body["data"]["last_name"] == "test"
    assert body["data"]["avatar"] == "https://reqres.in/img/faces/2-image.jpg"
