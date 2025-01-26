import time

from selenium.webdriver.support import expected_conditions as EC
from _pytest.fixtures import fixture
from api_clients.user_client.models.requests.user import User
from tests.singleton import WebDriverSingleton
from tests.test_base_ui import TestBaseUi


class TestUILoginPage(TestBaseUi):

    @fixture
    def open_and_close_browser_fixture(self):
        WebDriverSingleton.get_driver()
        WebDriverSingleton.get_driver().get(self.base_page.base_url)
        yield
        WebDriverSingleton.quit_driver()

    def test_user_cannot_login_with_empty_fields(self, open_and_close_browser_fixture):
        self.login_page.login(User(email="", password=""))
        time.sleep(1)
        error = self.login_page.find_error()
        assert error == 'Incorrect username or password'

    def test_cannot_login_unregistered_user(self, open_and_close_browser_fixture):
        user = self.random_user.generate()
        self.login_page.login(User(email=user.email, password=user.password))
        time.sleep(1)
        error = self.login_page.find_error()
        assert error == 'Incorrect username or password'

    def test_cannot_login_without_email_field(self, open_and_close_browser_fixture):
        user = self.random_user.generate()
        self.login_page.login(User(email='', password=user.password))
        time.sleep(1)
        error = self.login_page.find_error()
        assert error == 'Incorrect username or password'

    def test_cannot_login_without_password_field(self, open_and_close_browser_fixture):
        user = self.random_user.generate()
        self.login_page.login(User(email=user.email, password=''))
        time.sleep(1)
        error = self.login_page.find_error()
        assert error == 'Incorrect username or password'

    def test_sign_up_button(self, open_and_close_browser_fixture):
        self.login_page.click_on_sing_up_button()
        assert WebDriverSingleton.wait_for_element(self.login_page.base_url, self.login_page.contact_url, EC.url_changes), "Sign up page is open."

    def test_login_user(self, open_and_close_browser_fixture):
        user = self.random_user.generate()
        self.login_page.login(User(email=user.email, password=user.password))
        assert WebDriverSingleton.wait_for_element(self.login_page.base_url, self.login_page.contact_url, EC.url_changes), "User successfully login!"

