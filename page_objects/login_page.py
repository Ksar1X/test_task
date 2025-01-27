from selenium.webdriver.common.by import By
from api_clients.user_client.models.requests.user import User
from page_objects.base_page import BasePage
from page_objects.element import Element


class LoginPage(BasePage):

    email_field = Element((By.ID, "email"))
    password_field = Element((By.ID, "password"))
    sing_up_button = Element((By.ID, "signup"))


    def login(self, user:User):
        self.email_field.send_text(user.email)
        self.password_field.send_text(user.password)
        self.click_on_submit_button()

    def click_on_sing_up_button(self):
        self.sing_up_button.click_on_element()

