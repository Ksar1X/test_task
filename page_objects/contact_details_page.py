from page_objects.base_page import BasePage


class ContactDetailsPage(BasePage):

    EDIT_CONTACT_BUTTON = ("xpath", "//button[@id='edit-contact']")
    DELETE_CONTACT_BUTTON = ("xpath", "//button[@id='delete']")
    RETURN_TO_CONTACT_LIST_BUTTON = ("xpath", "//button[@id='return']")

    def return_to_contact_list_page(self):
        self.driver.find_element(*self.RETURN_TO_CONTACT_LIST_BUTTON).click()

    def go_to_edit_contact_page(self):
        self.driver.find_element(*self.EDIT_CONTACT_BUTTON).click()

    def delete_contact(self):
        self.driver.find_element(*self.DELETE_CONTACT_BUTTON).click()
        self.driver.switch_to.alert.accept()