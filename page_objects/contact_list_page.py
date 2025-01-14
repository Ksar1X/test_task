from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.element import Element


class ContactListPage(BasePage):

    CONTACT_ROW = ("xpath", "//td[1]")

    def add_contact(self):
        element = Element((By.ID, "add-contact"))
        web_element = element.find(self.driver)
        web_element.click()

    def click_on_contact(self, email):
        self.driver.find_element("xpath",f"//td[contains(text(),'{email}')]").click()