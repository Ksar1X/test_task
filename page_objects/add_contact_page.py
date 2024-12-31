from api_clients.contact_client.models.requests.create_contact_model import CreateContact
from page_objects.base_page import BasePage


class AddContactPage(BasePage):
    CONTACT_FIRST_NAME_FIELD = ("xpath", "//input[@id='firstName']")
    CONTACT_LAST_NAME_FIELD = ("xpath", "//input[@id='lastName']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    ERROR = ("xpath", "//span[@id='error']")

    def add_new_contact(self, contact:CreateContact):
        first_name_field = self.driver.find_element(*self.CONTACT_FIRST_NAME_FIELD)
        first_name_field.send_keys(contact.firstName)
        first_name_field = self.driver.find_element(*self.CONTACT_LAST_NAME_FIELD)
        first_name_field.send_keys(contact.lastName)
        self.click_on_submit_button()

    def click_on_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def error(self):
        return self.driver.find_element(*self.ERROR)