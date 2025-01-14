from selenium.webdriver.common.by import By

from api_clients.contact_client.models.requests.contact_model import ContactModel
from page_objects.contact_list_page import ContactListPage
from page_objects.element import Element


class AddContactPage(ContactListPage):

    def add_new_contact(self, contact:ContactModel):
        element = Element((By.ID, "firstName"))
        web_element = element.find(self.driver)
        web_element.send_keys(contact.firstName)
        element = Element((By.ID, "lastName"))
        web_element = element.find(self.driver)
        web_element.send_keys(contact.lastName)

    def click_on_submit_button(self):
        element = Element((By.ID, "submit"))
        web_element = element.find(self.driver)
        web_element.click()

    def error(self):
        element = Element((By.ID, "error"))
        web_element = element.find(self.driver)
        return web_element.text

    def click_on_cancel_button(self):
        element = Element((By.ID, "error"))
        web_element = element.find(self.driver)
        web_element.click()