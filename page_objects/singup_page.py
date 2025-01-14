from selenium.webdriver.common.by import By

from api_clients.user_client.models.requests.create_user_model import CreateUser
from page_objects.base_page import BasePage
from page_objects.element import Element


class SingUpPage(BasePage):

    def open_browser(self):
        self.driver.get(self.sing_up_url)

    def click_on_submit_button(self):
        element = Element((By.ID, "submit"))
        web_element = element.find(self.driver)
        web_element.click()

    def create_user(self, user:CreateUser):
        self.open_browser()
        element = Element((By.ID, "firstName"))
        web_element = element.find(self.driver)
        web_element.send_keys(user.firstName)
        element = Element((By.ID, "lastName"))
        web_element = element.find(self.driver)
        web_element.send_keys(user.lastName)
        element = Element((By.ID, "email"))
        web_element = element.find(self.driver)
        web_element.send_keys(user.email)
        element = Element((By.ID, "password"))
        web_element = element.find(self.driver)
        web_element.send_keys(user.password)
        self.click_on_submit_button()

    def click_on_cancel_button(self):
        element = Element((By.ID, "cancel"))
        web_element = element.find(self.driver)
        web_element.click()

    def error(self):
        element = Element((By.ID, "error"))
        web_element = element.find(self.driver)
        return web_element.text