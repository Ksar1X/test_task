from selenium.webdriver.common.by import By

from api_clients.user_client.models.requests.user import User
from page_objects.base_page import BasePage
from page_objects.element import Element


class LoginPage(BasePage):

    def open_browser(self):
        self.driver.get(self.base_url)

    def close_browser(self):
        self.driver.quit()


    def click_on_submit_button(self):
        element = Element((By.ID, "submit"))
        web_element = element.find(self.driver)
        web_element.click()

    def login(self, user:User):
        self.open_browser()
        element = Element((By.ID, "email"))
        web_element = element.find(self.driver)
        web_element.send_keys(user.email)
        element = Element((By.ID, "password"))
        web_element = element.find(self.driver)
        web_element.send_keys(user.password)
        self.click_on_submit_button()


    def click_on_sing_up_button(self):
        element = Element((By.ID, "signup"))
        web_element = element.find(self.driver)
        web_element.click()

    def error(self):
        element = Element((By.ID, "error"))
        web_element = element.find(self.driver)
        return web_element.text
