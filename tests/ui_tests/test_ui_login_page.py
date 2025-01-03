from selenium.webdriver.support import expected_conditions as EC

from tests.test_base_ui import TestBaseUi


class TestUILoginPage(TestBaseUi):


    def test_user_cannot_login_with_empty_fields(self):
        self.login_page.login(email="", password="")
        error = self.login_page.find_error()
        assert error is not None

    def test_cannot_login_unregistered_user(self):
        user = self.random_user.generate()
        self.login_page.login(email=user.email, password=user.password)
        error = self.login_page.find_error()
        assert error is not None

    def test_cannot_login_without_email_field(self):
        user = self.random_user.generate()
        self.login_page.login(email='', password=user.password)
        error = self.login_page.find_error()
        assert error is not None

    def test_cannot_login_without_password_field(self):
        user = self.random_user.generate()
        self.login_page.login(email=user.email, password='')
        error = self.login_page.find_error()
        assert error is not None

    def test_sign_up_button(self):
        self.login_page.click_on_singup_button()
        assert self.login_page.wait.until(EC.url_changes(self.login_page.contact_url))

    def test_login_user(self):
        self.login_page.login(email="garynychxxx@gmail.com", password="raketa123")
        assert self.login_page.wait.until(EC.url_changes(self.login_page.contact_url))
