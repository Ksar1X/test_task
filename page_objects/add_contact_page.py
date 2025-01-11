from page_objects.base_page import BasePage
from page_objects.contact_list_page import ContactListPage


class AddContactPage(ContactListPage):
    CONTACT_FIRST_NAME_FIELD = ("xpath", "//input[@id='firstName']")
    CONTACT_LAST_NAME_FIELD = ("xpath", "//input[@id='lastName']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    CANCEL_BUTTON = ("xpath", "//button[@id='cancel']")
    ERROR = ("xpath", "//span[@id='error']")

    def add_new_contact(self, contact):
        first_name_field = self.driver.find_element(*self.CONTACT_FIRST_NAME_FIELD)
        first_name_field.send_keys(contact.firstName)
        last_name_field = self.driver.find_element(*self.CONTACT_LAST_NAME_FIELD)
        last_name_field.send_keys(contact.lastName)
        self.click_on_submit_button()

    def click_on_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def error(self):
        error = self.driver.find_element(*self.ERROR)
        return error.text

    def click_on_cancel_button(self):
        self.driver.find_element(*self.CANCEL_BUTTON).click()