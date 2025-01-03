from page_objects.base_page import BasePage


class ContactListPage(BasePage):

    ADD_CONTACT_BUTTON = ("xpath", "//button[@id='add-contact']")
    CONTACT_ROW = ("xpath", "//td[1]")

    def add_contact(self):
        self.driver.find_element(*self.ADD_CONTACT_BUTTON).click()

    def click_on_contact(self, email):
        self.driver.find_element("xpath",f"//td[contains(text(),'{email}')]").click()