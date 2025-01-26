import time

from selenium.webdriver.common.by import By

from api_clients.user_client.models.requests.user import User
from page_objects.base_page import BasePage
from page_objects.element import Element


class LoginPage(BasePage):

    email_field = Element((By.ID, "email"))
    password_field = Element((By.ID, "password"))
    sing_up_button = Element((By.ID, "signup"))

    submit_button = Element((By.ID, "submit"))

    error = Element((By.ID, "error"))

    def login(self, user:User):
        self.email_field.send_text(user.email)
        self.password_field.send_text(user.password)
        self.submit_button.click()

    def click_on_sing_up_button(self):
        self.sing_up_button.click()

    def find_error(self):
        return self.error.get_text()
