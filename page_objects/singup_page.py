from selenium.webdriver.common.by import By

from api_clients.user_client.models.requests.create_user_model import CreateUser
from page_objects.base_page import BasePage
from page_objects.element import Element


class SingUpPage(BasePage):

    submit_button = Element((By.ID, "submit"))
    cancel_button = Element((By.ID, "cancel"))

    first_name_field = Element((By.ID, "firstName"))
    last_name_field = Element((By.ID, "lastName"))
    email_field = Element((By.ID, "email"))
    password_field = Element((By.ID, "password"))

    error = Element((By.ID, "error"))

    def create_user(self, user:CreateUser):
        self.first_name_field.send(user.firstName)
        self.last_name_field.send(user.lastName)
        self.email_field.send(user.email)
        self.password_field.send(user.password)
        self.submit_button.click()


    def find_error(self):
        return self.error.get_text()