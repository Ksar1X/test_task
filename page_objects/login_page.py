from api_clients.user_client.models.requests.user import User
from page_objects.base_page import BasePage


class LoginPage(BasePage):

    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    SIGN_UP_BUTTON = ("xpath", "//button[@id='signup']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    ERROR = ("xpath", "//span[@id='error']")



    def open_browser(self):
        self.driver.get(self.base_url)


    def click_on_submit_button(self):
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        button.click()

    def login(self, email, password):
        self.open_browser()
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(password)
        self.click_on_submit_button()


    def click_on_singup_button(self):
        button = self.driver.find_element(*self.SIGN_UP_BUTTON)
        button.click()

    def find_error(self):
        return self.driver.find_element(*self.ERROR)