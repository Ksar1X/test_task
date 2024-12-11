from page_objects.base_page import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC


class TestUILoginPage(BasePage):

    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    SIGN_UP_BUTTON = ("xpath", "//button[@id='signup']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    ERROR = ("xpath", "//span[@id='error']")


    def test_user_cannot_login_with_empty_fields(self):
        self.driver.get(self.base_url)
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()
        error = self.driver.find_element(*self.ERROR)
        assert error is not None

    def test_cannot_login_unregistered_user(self):
        self.driver.get(self.base_url)
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys("auoifhqw@g.com")
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys("joiafsajs")
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()
        error = self.driver.find_element(*self.ERROR)
        assert error is not None

    def test_cannot_login_without_email_field(self):
        self.driver.get(self.base_url)
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys("joiafsajs")
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()
        error = self.driver.find_element(*self.ERROR)
        assert error is not None

    def test_cannot_login_without_password_field(self):
        self.driver.get(self.base_url)
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys("auoifhqw@g.com")
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()
        error = self.driver.find_element(*self.ERROR)
        assert error is not None

    def test_sign_up_button(self):
        self.driver.get(self.base_url)
        button = self.driver.find_element(*self.SIGN_UP_BUTTON)
        button.click()
        assert button is not None

    def test_login_user(self):
        self.driver.get(self.base_url)
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys("garynychxxx@gmail.com")
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys("raketa123")
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()
        assert self.wait.until(EC.url_changes(self.base_url + "/contactList"))
