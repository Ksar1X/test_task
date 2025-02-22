from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.element import Element
from tests.webdriver_singleton import WebDriverSingleton


class ContactDetailsPage(BasePage):

    edit_contact_button = Element((By.ID, "edit-contact"))
    delete_contact_button = Element((By.ID, "delete"))
    return_to_contact_list_button = Element((By.ID, "return"))

    def return_to_contact_list_page(self):
        self.return_to_contact_list_button.click_on_element()

    def go_to_edit_contact_page(self):
        self.edit_contact_button.click_on_element()

    def delete_contact(self):
        self.delete_contact_button.click_on_element()
        WebDriverSingleton.get_driver().switch_to.alert.accept()