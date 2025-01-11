from selenium.webdriver import Keys
from page_objects.contact_details_page import ContactDetailsPage


class EditContactPage(ContactDetailsPage):
    FIRST_NAME_FIELD = ("xpath", "//input[@id='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@id='lastName']")
    DATE_OF_BIRTH_FIELD = ("xpath", "//input[@id='birthdate']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    PHONE_FIELD = ("xpath", "//input[@id='phone']")
    STREET1_FIELD = ("xpath", "//input[@id='street1']")
    STREET2_FIELD = ("xpath", "//input[@id='street2']")
    CITY_FIELD = ("xpath", "//input[@id='city']")
    STATE_FIELD = ("xpath", "//input[@id='stateProvince']")
    POSTAL_CODE_FIELD = ("xpath", "//input[@id='postalCode']")
    COUNTRY_FIELD = ("xpath", "//input[@id='country']")

    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    CANCEL_BUTTON = ("xpath", "//button[@id='cancel']")

    def change_first_name_field(self, message):
        first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        self.actions.click(first_name_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        first_name_field.send_keys(message)
        self.click_on_submit_button()

    def change_last_name_field(self, message):
        last_name_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        self.actions.click(last_name_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        last_name_field.send_keys(message)
        self.click_on_submit_button()

    def change_birth_date_field(self, message):
        birth_date_field = self.driver.find_element(*self.DATE_OF_BIRTH_FIELD)
        self.actions.click(birth_date_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        birth_date_field.send_keys(message)
        self.click_on_submit_button()

    def change_email_field(self, message):
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        self.actions.click(email_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        email_field.send_keys(message)
        self.click_on_submit_button()

    def change_phone_field(self, message):
        phone_field = self.driver.find_element(*self.PHONE_FIELD)
        self.actions.click(phone_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        phone_field.send_keys(message)
        self.click_on_submit_button()

    def change_street1_field(self, message):
        street1_field = self.driver.find_element(*self.STREET1_FIELD)
        self.actions.click(street1_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        street1_field.send_keys(message)
        self.click_on_submit_button()

    def change_street2_field(self, message):
        street2_field = self.driver.find_element(*self.STREET2_FIELD)
        self.actions.click(street2_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        street2_field.send_keys(message)
        self.click_on_submit_button()

    def change_city_field(self, message):
        city_field = self.driver.find_element(*self.CITY_FIELD)
        self.actions.click(city_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        city_field.send_keys(message)
        self.click_on_submit_button()

    def change_state_province_field(self, message):
        sp_field = self.driver.find_element(*self.STATE_FIELD)
        self.actions.click(sp_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        sp_field.send_keys(message)
        self.click_on_submit_button()

    def change_postal_code_field(self, message):
        pc_field = self.driver.find_element(*self.POSTAL_CODE_FIELD)
        self.actions.click(pc_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        pc_field.send_keys(message)
        self.click_on_submit_button()

    def change_country_field(self, message):
        country_field = self.driver.find_element(*self.COUNTRY_FIELD)
        self.actions.click(country_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        country_field.send_keys(message)
        self.click_on_submit_button()

    def click_on_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def click_on_cancel_button(self):
        self.driver.find_element(*self.CANCEL_BUTTON).click()

