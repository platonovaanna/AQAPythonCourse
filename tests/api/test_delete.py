import requests

from clients import users_api
from pages.login_page import LoginPage
def test_delete_user(users_api):
    payload = {
        "data": {
            "email": "test.weaver_update@reqres.in",
            "first_name": "test_update",
            "last_name": "test_update",
            "avatar": "https://reqres.in/img/faces/2-image_update.jpg"
        }
    }
    response_create = users_api.create_user(payload)
    assert response_create.status_code == 201
    body = response_create.json()
    user_id = body["id"]
    response_delete = users_api.delete_user(user_id)
    assert response_delete.status_code == 204
