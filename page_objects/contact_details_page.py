from selenium.webdriver.common.by import By

from page_objects.contact_list_page import ContactListPage
from page_objects.element import Element


class ContactDetailsPage(ContactListPage):

    EDIT_CONTACT_BUTTON = ("xpath", "//button[@id='edit-contact']")
    DELETE_CONTACT_BUTTON = ("xpath", "//button[@id='delete']")
    RETURN_TO_CONTACT_LIST_BUTTON = ("xpath", "//button[@id='return']")

    def return_to_contact_list_page(self):
        element = Element((By.ID, "return"))
        web_element = element.find(self.driver)
        web_element.click()

    def go_to_edit_contact_page(self):
        element = Element((By.ID, "edit-contact"))
        web_element = element.find(self.driver)
        web_element.click()

    def delete_contact(self):
        element = Element((By.ID, "delete"))
        web_element = element.find(self.driver)
        web_element.click()
        self.driver.switch_to.alert.accept()