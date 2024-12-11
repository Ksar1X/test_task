from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class TestUISingUpPage(BasePage):

    FIRST_NAME_FIELD = ("xpath", "//input[@id='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@id='lastName']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    CANCEL_BUTTON = ("xpath", "//button[@id='cancel']")
    ERROR = ("xpath", "//span[@id='error']")


    def test_user_cannot_create_without_empty_fields(self):
        self.driver.get(self.sing_up_url)
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()
        error = self.driver.find_element(*self.ERROR)
        assert error is not None

    def test_user_cannot_create_without_first_name_field(self):
        self.driver.get(self.sing_up_url)
        last_name_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        last_name_field.send_keys("Fake")
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys("Fake@gmail.com")
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys("Fake1234")
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()
        error = self.driver.find_element(*self.ERROR)
        assert error is not None

    def test_user_cannot_create_without_last_name_field(self):
        self.driver.get(self.sing_up_url)
        first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        first_name_field.send_keys("Fake")
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys("Fake@gmail.com")
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys("Fake1234")
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()
        error = self.driver.find_element(*self.ERROR)
        assert error is not None

    def test_user_cannot_create_without_email_field(self):
        self.driver.get(self.sing_up_url)
        first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        first_name_field.send_keys("Fake")
        last_name_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        last_name_field.send_keys("Fake")
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys("Fake1234")
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()
        error = self.driver.find_element(*self.ERROR)
        assert error is not None

    def test_user_cannot_create_without_password_field(self):
        self.driver.get(self.sing_up_url)
        first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        first_name_field.send_keys("Fake")
        last_name_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        last_name_field.send_keys("Fake")
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys("Fake@gmail.com")
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()
        error = self.driver.find_element(*self.ERROR)
        assert error is not None

    def test_sing_up(self):
        self.driver.get(self.sing_up_url)
        first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        first_name_field.send_keys("Fake")
        last_name_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        last_name_field.send_keys("Fake")
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys("Fake@gmail.com")
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys("Fake1234")
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()
        assert self.wait.until(EC.url_changes(self.contact_url))

    def test_cancel_button(self):
        self.driver.get(self.sing_up_url)
        button = self.driver.find_element(*self.CANCEL_BUTTON)
        button.click()
        assert self.wait.until(EC.url_changes(self.base_url))