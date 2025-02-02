from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.element import Element
from tests.webdriver_singleton import WebDriverSingleton


class ContactListPage(BasePage):

    add_contact_button = Element((By.ID, "add-contact"))

    def add_contact(self):
        self.add_contact_button.click_on_element()

    @staticmethod
    def click_on_contact(email):
        WebDriverSingleton.get_driver().find_element("xpath",f"//td[contains(text(),'{email}')]").click()
