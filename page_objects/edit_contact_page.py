import time
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.element import Element



class EditContactPage(BasePage):

    first_name_field = Element((By.ID, "firstName"))
    last_name_field = Element((By.ID, "lastName"))
    birthdate_field = Element((By.ID, "birthdate"))
    email_field = Element((By.ID, "email"))
    phone_field = Element((By.ID, "phone"))
    street1_field = Element((By.ID, "street1"))
    street2_field = Element((By.ID, "street2"))
    city_field = Element((By.ID, "city"))
    state_field = Element((By.ID, "stateProvince"))
    postal_code_field = Element((By.ID, "postalCode"))
    country_field = Element((By.ID, "country"))

    @staticmethod
    def clear_and_input(field: Element, message: str):
        elem = field.find()
        elem.click()
        time.sleep(1)
        elem.clear()
        time.sleep(1)
        field.send_text(message)

    def update_field(self, field_name: str, message: str):
        field = getattr(self, f"{field_name}_field", None)
        self.clear_and_input(field, message)
        self.click_on_submit_button()
