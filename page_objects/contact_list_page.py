from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.element import Element


class ContactListPage(BasePage):

    add_contact_button = Element((By.ID, "add_contact"))

    def add_contact(self):
        self.add_contact_button.click()

    def click_on_contact(self, email):
        self.driver.find_element("xpath",f"//td[contains(text(),'{email}')]").click()
