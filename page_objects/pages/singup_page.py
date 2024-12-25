from api_clients.user_client.models.requests.create_user_model import CreateUser
from page_objects.pages.base_page import BasePage


class SingUpPage(BasePage):

    FIRST_NAME_FIELD = ("xpath", "//input[@id='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@id='lastName']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")

    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    CANCEL_BUTTON = ("xpath", "//button[@id='cancel']")

    ERROR = ("xpath", "//span[@id='error']")


    def open_page(self):
        self.driver.get(self.sing_up_url)

    def click_on_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def create_user(self, user:CreateUser):
        self.open_page()
        first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        first_name_field.send_keys(user.firstName)
        last_name_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        last_name_field.send_keys(user.lastName)
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(user.email)
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(user.password)
        self.click_on_submit_button()

    def click_on_cancel_button(self):
        self.driver.get(self.sing_up_url)
        self.driver.find_element(*self.CANCEL_BUTTON).click()

    def find_error(self):
        return self.driver.find_element(*self.ERROR)