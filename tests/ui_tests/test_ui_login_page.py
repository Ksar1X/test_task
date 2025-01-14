import time

from selenium.webdriver.support import expected_conditions as EC

from api_clients.user_client.models.requests.user import User
from tests.test_base_ui import TestBaseUi


class TestUILoginPage(TestBaseUi):

    def test_user_cannot_login_with_empty_fields(self):
        self.login_page.login(User(email="", password=""))
        time.sleep(1)
        error = self.login_page.error()
        assert error == 'Incorrect username or password'

    def test_cannot_login_unregistered_user(self):
        user = self.random_user.generate()
        self.login_page.login(User(email=user.email, password=user.password))
        time.sleep(1)
        error = self.login_page.error()
        assert error == 'Incorrect username or password'

    def test_cannot_login_without_email_field(self):
        user = self.random_user.generate()
        self.login_page.login(User(email='', password=user.password))
        time.sleep(1)
        error = self.login_page.error()
        assert error == 'Incorrect username or password'

    def test_cannot_login_without_password_field(self):
        user = self.random_user.generate()
        self.login_page.login(User(email=user.email, password=''))
        time.sleep(1)
        error = self.login_page.error()
        assert error == 'Incorrect username or password'

    def test_sign_up_button(self):
        self.login_page.click_on_sing_up_button()
        assert self.login_page.wait.until(EC.url_changes(self.login_page.contact_url)), "Sign up page is open."

    def test_login_user(self):
        user = self.random_user.generate()
        self.login_page.login(User(email=user.email, password=user.password))
        assert self.login_page.wait.until(EC.url_changes(self.login_page.contact_url)), "User successfully login!"
