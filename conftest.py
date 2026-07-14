import pytest
from playwright.sync_api import sync_playwright

from clients.users_api import UsersApi


@pytest.fixture
def api_headers():
    print("\nSetup: preparing API session/token")

    headers = {
        "Content-Type": "application/json",
        "x-api-key": "YOUR_API_KEY"
    }

    yield headers

    print("\nTeardown: cleanup after API test")


@pytest.fixture
def users_api(api_headers):
    return UsersApi(
        base_url="https://reqres.in/api",
        headers=api_headers
    )


@pytest.fixture
def page():
    with sync_playwright() as p:
        print("\nSetup: Launching browser")

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

        browser.close()
        print("\nTeardown: cleanup after UI test")