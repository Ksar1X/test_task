from selenium.webdriver.common.by import By

from page_objects.contact_list_page import ContactListPage
from page_objects.element import Element


class ContactDetailsPage(ContactListPage):

    edit_contact_button = Element((By.ID, "edit-contact"))
    delete_contact_button = Element((By.ID, "delete"))

    return_to_contact_list_button = Element((By.ID, "return"))

    def return_to_contact_list_page(self):
        self.return_to_contact_list_button.click()

    def go_to_edit_contact_page(self):
        self.edit_contact_button.click()

    def delete_contact(self):
        self.delete_contact_button.click()
        self.driver.switch_to.alert.accept()