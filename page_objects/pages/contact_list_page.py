from tests.test_base_ui import BaseUiTest


class ContactListPage(BaseUiTest):

    ADD_CONTACT_BUTTON = ("xpath", "//button[@id='add-contact']")

    CONTACT_ROW = ("xpath", "//td[1]")



    def delete_contact(self):
        contact_box = self.driver.find_element(*self.CONTACT_ROW)
        contact_box.click()








