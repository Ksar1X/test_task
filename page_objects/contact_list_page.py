from api_clients.contact_client.models.requests.create_contact_model import CreateContact
from page_objects.base_page import BasePage


class ContactListPage(BasePage):

    ADD_CONTACT_BUTTON = ("xpath", "//button[@id='add-contact']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    CANCEL_BUTTON = ("xpath", "//button[@id='cancel']")
    DELETE_BUTTON = ("xpath", "//*[@id='myTable']/tr[1]")

    CONTACT_ROW = ("xpath", "//tr[@class='contactTableBodyRow']")
    FIRST_NAME_FIELD = ("xpath", "//input[@id='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@id='lastName']")
    BIRTHDATE_FIELD = ("xpath", "//input[@id='birthdate']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    PHONE_FIELD = ("xpath", "//input[@id='phone']")
    FIRST_STREET_FIELD = ("xpath", "//input[@id='street1']")
    SECOND_STREET_FIELD = ("xpath", "//input[@id='street2']")
    CITY_FIELD = ("xpath", "//input[@id='city']")
    STATE_PROVINCE_FIELD = ("xpath", "//input[@id='stateProvince']")
    POSTAL_CODE_FIELD = ("xpath", "//input[@id='postalCode']")
    COUNTRY_FIELD = ("xpath", "//input[@id='country']")

    ERROR = ("xpath", "//span[@id='error']")

    def open_page(self):
        self.driver.get(self.contact_url)

    def click_on_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def create_contact(self, contact: CreateContact):
        self.open_page()
        self.driver.find_element(*self.ADD_CONTACT_BUTTON).click()
        first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        first_name_field.send_keys(contact.firstName)
        second_name_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        second_name_field.send_keys(contact.lastName)
        birthdate_field = self.driver.find_element(*self.BIRTHDATE_FIELD)
        birthdate_field.send_keys(contact.birthdate)
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(contact.email)
        phone_field = self.driver.find_element(*self.PHONE_FIELD)
        phone_field.send_keys(contact.phone)
        first_street_field = self.driver.find_element(*self.FIRST_STREET_FIELD)
        first_street_field.send_keys(contact.street1)
        second_street_field = self.driver.find_element(*self.SECOND_STREET_FIELD)
        second_street_field.send_keys(contact.street2)
        city_field = self.driver.find_element(*self.CITY_FIELD)
        city_field.send_keys(contact.city)
        state_field = self.driver.find_element(*self.STATE_PROVINCE_FIELD)
        state_field.send_keys(contact.stateProvince)
        postal_field = self.driver.find_element(*self.POSTAL_CODE_FIELD)
        postal_field.send_keys(contact.postalCode)
        country_field = self.driver.find_element(*self.COUNTRY_FIELD)
        country_field.send_keys(contact.country)
        self.click_on_submit_button()

    def find_error(self):
        return self.driver.find_element(*self.ERROR)

    def delete_contact(self):
        self.open_page()
        self.driver.find_element(*self.CONTACT_ROW).click()
        self.driver.find_element(*self.DELETE_BUTTON).click()





