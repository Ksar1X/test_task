from selenium.webdriver.common.by import By
from api_clients.user_client.models.requests.create_user_model import CreateUser
from page_objects.base_page import BasePage
from page_objects.element import Element


class SingUpPage(BasePage):

    first_name_field = Element((By.ID, "firstName"))
    last_name_field = Element((By.ID, "lastName"))
    email_field = Element((By.ID, "email"))
    password_field = Element((By.ID, "password"))


    def create_user(self, user:CreateUser):
        self.first_name_field.send_text(user.firstName)
        self.last_name_field.send_text(user.lastName)
        self.email_field.send_text(user.email)
        self.password_field.send_text(user.password)
        self.click_on_submit_button()
