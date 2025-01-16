from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from page_objects.contact_details_page import ContactDetailsPage
from page_objects.element import Element


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
    postal_code_field = Element((By.ID, "postalCode'"))
    country_field = Element((By.ID, "country'"))

    submit_button = Element((By.ID, "submit'"))
    cancel_button = Element((By.ID, "cancel"))

    def change_first_name_field(self, message):
        field = self.first_name_field.find()
        self.actions.click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.first_name_field.send(message)
        self.submit_button.click()

    def change_last_name_field(self, message):
        field = self.last_name_field.find()
        self.actions.click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.last_name_field.send(message)
        self.submit_button.click()

    def change_birth_date_field(self, message):
        field = self.birthdate_field.find()
        self.actions.click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.birthdate_field.send(message)
        self.submit_button.click()

    def change_email_field(self, message):
        field = self.email_field.find()
        self.actions.click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.email_field.send(message)
        self.submit_button.click()


    def change_phone_field(self, message):
        field = self.phone_field.find()
        self.actions.click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.phone_field.send(message)
        self.submit_button.click()

    def change_street1_field(self, message):
        field = self.street1_field.find()
        self.actions.click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.street1_field.send(message)
        self.submit_button.click()

    def change_street2_field(self, message):
        field = self.street2_field.find()
        self.actions.click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.street2_field.send(message)
        self.submit_button.click()

    def change_city_field(self, message):
        field = self.city_field.find()
        self.actions.click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.city_field.send(message)
        self.submit_button.click()

    def change_state_province_field(self, message):
        field = self.state_field.find()
        self.actions.click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.state_field.send(message)
        self.submit_button.click()

    def change_postal_code_field(self, message):
        field = self.postal_code_field.find()
        self.actions.click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.postal_code_field.send(message)
        self.submit_button.click()

    def change_country_field(self, message):
        field = self.country_field.find()
        self.actions.click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.country_field.send(message)
        self.submit_button.click()

