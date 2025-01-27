from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from page_objects.contact_details_page import ContactDetailsPage
from page_objects.element import Element
from tests.singleton import WebDriverSingleton


class EditContactPage(ContactDetailsPage):

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
        field.click_on_element()
        action = WebDriverSingleton.get_action_chain()
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        field.send_text(message)

    def update_field(self, field_name: str, message: str):
        field = getattr(self, f"{field_name}_field", None)
        self.clear_and_input(field, message)
        self.click_on_submit_button()

    def change_first_name_field(self, message: str):
        self.update_field("first_name", message)

    def change_last_name_field(self, message: str):
        self.update_field("last_name", message)

    def change_birth_date_field(self, message: str):
        self.update_field("birthdate", message)

    def change_email_field(self, message: str):
        self.update_field("email", message)

    def change_phone_field(self, message: str):
        self.update_field("phone", message)

    def change_street1_field(self, message: str):
        self.update_field("street1", message)

    def change_street2_field(self, message: str):
        self.update_field("street2", message)

    def change_city_field(self, message: str):
        self.update_field("city", message)

    def change_state_province_field(self, message: str):
        self.update_field("state", message)

    def change_postal_code_field(self, message: str):
        self.update_field("postal_code", message)

    def change_country_field(self, message: str):
        self.update_field("country", message)
