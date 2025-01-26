from selenium.webdriver.common.by import By

from api_clients.contact_client.models.requests.create_contact_model import CreateContact
from page_objects.contact_list_page import ContactListPage
from page_objects.element import Element


class AddContactPage(ContactListPage):

    contact_first_name_field = Element((By.ID, "firstName"))
    contact_last_name_field = Element((By.ID, "lastName"))

    submit_button = Element((By.ID, "submit"))
    cancel_button = Element((By.ID, "cancel"))

    error = Element((By.ID, "error"))

    def add_new_contact(self, contact:CreateContact):
        self.contact_first_name_field.send_text(contact.firstName)
        self.contact_last_name_field.send_text(contact.lastName)

    def click_on_submit_button(self):
        self.submit_button.click()

    def fiend_error(self):
        return self.error.get_text()

    def click_on_cancel_button(self):
        self.cancel_button.click()