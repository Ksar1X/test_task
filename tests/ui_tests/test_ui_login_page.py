from _pytest.fixtures import fixture
from api_clients.user_client.models.requests.user import User
from tests.webdriver_singleton import WebDriverSingleton
from tests.test_base_ui import TestBaseUi


class TestUILoginPage(TestBaseUi):

    @fixture(scope="function", autouse=True)
    def open_and_close_browser_fixture(self):
        WebDriverSingleton.get_driver()
        WebDriverSingleton.get_driver().get(self.base_page.base_url)
        yield
        WebDriverSingleton.quit_driver()


    def test_user_cannot_login_with_empty_fields(self):
        self.login_page.login(User(email="", password=""))
        self.base_page.assert_error_message('Incorrect username or password')

    def test_cannot_login_unregistered_user(self):
        user = self.random_user.generate()
        self.login_page.login(User(email=user.email, password=user.password))
        self.base_page.assert_error_message('Incorrect username or password')

    def test_cannot_login_without_email_field(self):
        user = self.random_user.generate()
        self.login_page.login(User(email='', password=user.password))
        self.base_page.assert_error_message('Incorrect username or password')

    def test_cannot_login_without_password_field(self):
        user = self.random_user.generate()
        self.login_page.login(User(email=user.email, password=''))
        self.base_page.assert_error_message('Incorrect username or password')

    def test_sign_up_button(self):
        self.login_page.click_on_sing_up_button()
        self.base_page.assert_url_changed(self.base_page.base_url, self.base_page.sing_up_url)

    def test_login_user(self):
        user = self.random_user.generate()
        self.login_page.login(User(email=user.email, password=user.password))
        self.base_page.assert_url_changed(self.base_page.base_url, self.base_page.contact_url)

