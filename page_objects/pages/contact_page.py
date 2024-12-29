from tests.test_base_ui import BaseUiTest


class ContactPage(BaseUiTest):

    DELETE_BUTTON = ("xpath", "//button[@id='delete']")

    def click_on_delete_button(self):
        self.driver.find_element(*self.DELETE_BUTTON).click()
        self.driver.switch_to.alert.accept()

