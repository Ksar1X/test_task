from selenium.webdriver.support import expected_conditions as EC
from page_objects.element import Element
from tests.singleton import WebDriverSingleton
from selenium.webdriver.common.by import By


class BasePage:

    base_url = "https://thinking-tester-contact-list.herokuapp.com"
    sing_up_url = "https://thinking-tester-contact-list.herokuapp.com/addUser"
    contact_url = "https://thinking-tester-contact-list.herokuapp.com/contactList"
    add_contact_url = "https://thinking-tester-contact-list.herokuapp.com/addContact"
    contact_details_url = "https://thinking-tester-contact-list.herokuapp.com/contactDetails"
    edit_contact_url = 'https://thinking-tester-contact-list.herokuapp.com/editContact'

    submit_button = Element((By.ID, "submit"))
    cancel_button = Element((By.ID, "cancel"))
    error = Element((By.ID, "error"))


    def error_message(self):
        return self.error.get_text()

    def click_on_cancel_button(self):
        self.cancel_button.click_on_element()

    def click_on_submit_button(self):
        self.submit_button.click_on_element()


    def assert_error_message(self, expected_message: str):
        WebDriverSingleton.wait_for_element(By.ID, 'error', EC.visibility_of_element_located)
        error = self.error_message()
        assert error == expected_message, f"Expected error: {expected_message}, but got: {error}"

    @staticmethod
    def assert_url_changed(current_url: str, expected_url: str):
        return WebDriverSingleton.wait_for_element(current_url, expected_url, EC.url_changes)