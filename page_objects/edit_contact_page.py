from page_objects.base_page import BasePage


class EditContactPage(BasePage):
    FIRST_NAME_FIELD = ("xpath", "//input=[@id='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input=[@id='lastName']")
    DATE_OF_BIRTH_FIELD = ("xpath", "//input=[@id='birthdate']")
    EMAIL_FIELD = ("xpath", "//input=[@id='email']")
    PHONE_FIELD = ("xpath", "//input=[@id='phone']")
    STREET1_FIELD = ("xpath", "//input=[@id='street1']")
    STREET2_FIELD = ("xpath", "//input=[@id='street2']")
    CITY_FIELD = ("xpath", "//input=[@id='city']")
    STATE_FIELD = ("xpath", "//input=[@id='stateProvince']")
    POSTAL_CODE_FIELD = ("xpath", "//input=[@id='postalCode']")
    COUNTRY_FIELD = ("xpath", "//input=[@id='country']")

    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    CANCEL_BUTTON = ("xpath", "//button[@id='cancel']")

    def change_first_name_field(self, message):
        first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        first_name_field.clear()
        first_name_field.send_keys(message)

    def change_last_name_field(self, message):
        last_name_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        last_name_field.clear()
        last_name_field.send_keys(message)

    def change_birth_date_field(self, message):
        birth_date_field = self.driver.find_element(*self.DATE_OF_BIRTH_FIELD)
        birth_date_field.clear()
        birth_date_field.send_keys(message)

    def change_email_field(self, message):
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(message)

    def change_phone_field(self, message):
        phone_field = self.driver.find_element(*self.PHONE_FIELD)
        phone_field.clear()
        phone_field.send_keys(message)

    def change_street1_field(self, message):
        street1_field = self.driver.find_element(*self.STREET1_FIELD)
        street1_field.clear()
        street1_field.send_keys(message)

    def change_street2_field(self, message):
        street2_field = self.driver.find_element(*self.STREET2_FIELD)
        street2_field.clear()
        street2_field.send_keys(message)

    def change_city_field(self, message):
        city_field = self.driver.find_element(*self.CITY_FIELD)
        city_field.clear()
        city_field.send_keys(message)

    def change_state_province_field(self, message):
        sp_field = self.driver.find_element(*self.STATE_FIELD)
        sp_field.clear()
        sp_field.send_keys(message)

    def change_postal_code_field(self, message):
        pc_field = self.driver.find_element(*self.POSTAL_CODE_FIELD)
        pc_field.clear()
        pc_field.send_keys(message)

    def change_country_field(self, message):
        country_field = self.driver.find_element(*self.COUNTRY_FIELD)
        country_field.clear()
        country_field.send_keys(message)

    def click_on_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def click_on_cancel_button(self):
        self.driver.find_element(*self.CANCEL_BUTTON).click()
