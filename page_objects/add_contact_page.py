from selenium.webdriver.common.by import By
from api_clients.contact_client.models.requests.create_contact_model import CreateContact
from page_objects.base_page import BasePage
from page_objects.element import Element


class AddContactPage(BasePage):

    contact_first_name_field = Element((By.ID, "firstName"))
    contact_last_name_field = Element((By.ID, "lastName"))

    def add_new_contact(self, contact:CreateContact):
        self.contact_first_name_field.send_text(contact.firstName)
        self.contact_last_name_field.send_text(contact.lastName)
        self.click_on_submit_button()
