from selenium.webdriver.support import expected_conditions as EC
from tests.test_base import BaseTest


class TestUISingUpPage(BaseTest):

    FIRST_NAME_FIELD = ("xpath", "//input[@id='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@id='lastName']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    CANCEL_BUTTON = ("xpath", "//button[@id='cancel']")
    ERROR = ("xpath", "//span[@id='error']")


    def test_user_cannot_create_without_empty_fields(self):
        self.singUp_page.create_user(email='', password='', last_name='', first_name='')
        error = self.singUp_page.find_error()
        assert error is not None

    def test_user_cannot_create_without_first_name_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(email=user.email, password=user.password, last_name=user.lastName, first_name='')
        error = self.singUp_page.find_error()
        assert error is not None

    def test_user_cannot_create_without_last_name_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(email=user.email, password=user.password, last_name='', first_name=user.firstName)
        error = self.singUp_page.find_error()
        assert error is not None

    def test_user_cannot_create_without_email_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(email='', password=user.password, last_name=user.lastName, first_name=user.firstName)
        error = self.singUp_page.find_error()
        assert error is not None

    def test_user_cannot_create_without_password_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(email=user.email, password='', last_name=user.lastName, first_name=user.firstName)
        error = self.singUp_page.find_error()
        assert error is not None

    def test_sing_up(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(email=user.email, password=user.password, last_name=user.lastName, first_name=user.firstName)
        assert self.singUp_page.wait.until(EC.url_changes(self.singUp_page.contact_url))

    def test_cancel_button(self):
        self.singUp_page.click_on_cancel_button()
        assert self.singUp_page.wait.until(EC.url_changes(self.singUp_page.base_url))