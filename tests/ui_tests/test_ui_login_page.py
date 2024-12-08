from page_objects.base_page import BasePage
import time

class TestUILoginPage(BasePage):

    def test_user_cannot_login_with_empty_fields(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com")
        submit_button = self.driver.find_element("xpath", "//button[1]")
        submit_button.click()
        error = self.driver.find_element("id", "error")
        assert error is not None
