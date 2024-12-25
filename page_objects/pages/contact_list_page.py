from page_objects.pages.base_page import BasePage


class ContactListPage(BasePage):

    ADD_CONTACT_BUTTON = ("xpath", "//button[@id='add-contact']")

    CONTACT_ROW = ("xpath", "//tr[@class='contactTableBodyRow']")



    def delete_contact(self):
        self.driver.find_element(*self.CONTACT_ROW).click()









