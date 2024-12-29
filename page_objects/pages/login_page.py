import time

from api_clients.user_client.models.requests.user import User
from tests.test_base_ui import BaseUiTest


class LoginPage(BaseUiTest):

    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    SIGN_UP_BUTTON = ("xpath", "//button[@id='signup']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    ERROR = ("xpath", "//span[@id='error']")



    def open_page(self):
        self.driver.get(self.base_url)

    def click_on_submit_button(self):
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()

    def login(self, user:User):
        self.open_page()
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(user.email)
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(user.password)
        self.click_on_submit_button()


    def click_on_sing_up_button(self):
        button = self.driver.find_element(*self.SIGN_UP_BUTTON)
        button.click()

    def find_error(self):
        return self.driver.find_element(*self.ERROR)