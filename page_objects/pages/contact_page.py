from page_objects.pages.base_page import BasePage


class ContactPage(BasePage):

    DELETE_BUTTON = ("xpath", "//button[@id='delete']")

    def click_on_delete_button(self):
        self.driver.find_element(*self.DELETE_BUTTON).click()
        self.driver.switch_to.alert.accept()

