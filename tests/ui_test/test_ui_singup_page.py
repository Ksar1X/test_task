from selenium.webdriver.support import expected_conditions as EC

from api_clients.user_client.models.requests.create_user_model import CreateUser
from tests.test_base_ui import BaseUiTest


class TestUISingUpPage(BaseUiTest):

    FIRST_NAME_FIELD = ("xpath", "//input[@id='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@id='lastName']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    CANCEL_BUTTON = ("xpath", "//button[@id='cancel']")
    ERROR = ("xpath", "//span[@id='error']")


    def test_user_cannot_create_without_empty_fields(self):
        self.singUp_page.create_user(CreateUser(email='', password='', lastName='', firstName=''))
        error = self.singUp_page.find_error()
        assert error is not None

    def test_user_cannot_create_without_first_name_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password=user.password, lastName=user.lastName, firstName=''))
        error = self.singUp_page.find_error()
        assert error is not None

    def test_user_cannot_create_without_last_name_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password=user.password, lastName='', firstName=user.firstName))
        error = self.singUp_page.find_error()
        assert error is not None

    def test_user_cannot_create_without_email_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email='', password=user.password, lastName=user.lastName, firstName=user.firstName))
        error = self.singUp_page.find_error()
        assert error is not None

    def test_user_cannot_create_without_password_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password='', lastName=user.lastName, firstName=user.firstName))
        error = self.singUp_page.find_error()
        assert error is not None

    def test_sing_up(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password=user.password, lastName=user.lastName, firstName=user.firstName))
        assert self.singUp_page.wait.until(EC.url_changes(self.singUp_page.contact_url))

    def test_cancel_button(self):
        self.singUp_page.click_on_cancel_button()
        assert self.singUp_page.wait.until(EC.url_changes(self.singUp_page.base_url))