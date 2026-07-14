import requests

from clients import users_api
from pages.login_page import LoginPage
def test_update_user(users_api):
    payload_create = {
        "data": {
            "email": "test.weaver@reqres.in",
            "first_name": "test",
            "last_name": "test",
            "avatar": "https://reqres.in/img/faces/2-image_update.jpg"
        }
    }
    response_create = users_api.create_user(payload_create)
    assert response_create.status_code == 201
    body = response_create.json()
    user_id = body["id"]
    payload_update = {
        "data": {
            "email": "test.weaver_update@reqres.in",
            "first_name": "test_update",
            "last_name": "test_update",
            "avatar": "https://reqres.in/img/faces/2-image_update.jpg"
        }
    }
    response_update = users_api.update_user(user_id,payload_update)
    assert response_update.status_code == 200
    body = response_update.json()
    assert body["data"]["email"] == "test.weaver_update@reqres.in"
    assert body["data"]["first_name"] == "test_update"
    assert body["data"]["last_name"] == "test_update"
    assert body["data"]["avatar"] == "https://reqres.in/img/faces/2-image_update.jpg"