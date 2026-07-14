from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_success_login(page):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login("tomsmith", "SuperSecretPassword!")

    expect(login_page.flash_message).to_contain_text(
        "You logged into a secure area!"
    )

    expect(login_page.logout_link).to_be_visible()


def test_failed_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("test", "test")

    expect(login_page.flash_message).to_contain_text(
        "Your username is invalid!")

def test_logout(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    login_page.logout()

    expect(login_page.flash_message).to_contain_text(
            "You logged out of the secure area!")