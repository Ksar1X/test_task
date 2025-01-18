import time

from _pytest.fixtures import fixture
from selenium.webdriver.support import expected_conditions as EC

from api_clients.user_client.models.requests.create_user_model import CreateUser
from tests.singleton import WebDriverSingleton
from tests.test_base_ui import TestBaseUi


class TestUISingUpPage(TestBaseUi):

    @fixture
    def open_and_close_browser_fixture(self):
        WebDriverSingleton.get_driver()
        WebDriverSingleton.get_driver().get(self.base_page.sing_up_url)
        yield
        WebDriverSingleton.quit_driver()

    def test_user_cannot_create_without_empty_fields(self, open_and_close_browser_fixture):
        browser = open_and_close_browser_fixture
        self.singUp_page.create_user(CreateUser(email='', password='', lastName='', firstName=''))
        time.sleep(1)
        error = self.singUp_page.find_error()
        assert error == 'User validation failed: firstName: Path `firstName` is required., lastName: Path `lastName` is required., email: Email is invalid, password: Path `password` is required.'


    def test_user_cannot_create_without_first_name_field(self, open_and_close_browser_fixture):
        browser = open_and_close_browser_fixture
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password=user.password, lastName=user.lastName, firstName=''))
        time.sleep(1)
        error = self.singUp_page.find_error()
        assert error == 'User validation failed: firstName: Path `firstName` is required.'


    def test_user_cannot_create_without_last_name_field(self, open_and_close_browser_fixture):
        browser = open_and_close_browser_fixture
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password=user.password, lastName='', firstName=user.firstName))
        time.sleep(1)
        error = self.singUp_page.find_error()
        assert error == 'User validation failed: lastName: Path `lastName` is required.'


    def test_user_cannot_create_without_email_field(self, open_and_close_browser_fixture):
        browser = open_and_close_browser_fixture
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email='', password=user.password, lastName=user.lastName, firstName=user.firstName))
        time.sleep(1)
        error = self.singUp_page.find_error()
        assert error == 'User validation failed: email: Email is invalid'


    def test_user_cannot_create_without_password_field(self, open_and_close_browser_fixture):
        browser = open_and_close_browser_fixture
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password='', lastName=user.lastName, firstName=user.firstName))
        time.sleep(1)
        error = self.singUp_page.find_error()
        assert error == 'User validation failed: password: Path `password` is required.'


    def test_sing_up(self, open_and_close_browser_fixture):
        browser = open_and_close_browser_fixture
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password=user.password, lastName=user.lastName, firstName=user.firstName))
        assert self.singUp_page.wait.until(EC.url_changes(self.singUp_page.contact_url)), "User successfully sing up!"
