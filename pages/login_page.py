

class LoginPage:
    LOGIN_URL = "https://the-internet.herokuapp.com/login"
    def __init__(self, page):
        self.page = page

        self.username_input =self.page.locator("#username")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.flash_message = self.page.locator("#flash")
        self.logout_link = self.page.get_by_role("link", name="Logout")

    def open(self):
        self.page.goto(self.LOGIN_URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_link.click()

