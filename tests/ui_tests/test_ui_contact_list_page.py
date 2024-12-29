from tests.test_base import BaseTest
from selenium.webdriver.support import expected_conditions as EC

class TestUIContactListPage(BaseTest):

    def test_add_contact_to_contact_list(self):
        contact = self.random_contact.generate()
        self.contact_list_page.create_contact(first_name=contact.firstName, second_name=contact.lastName, birthdate=contact.birthdate, email=contact.email, phone=contact.phone, first_street=contact.street1, second_street=contact.street2, city=contact.city, state=contact.stateProvince, postal_code=contact.postalCode, country=contact.country)
        assert self.contact_list_page.wait.until(EC.url_changes(self.login_page.contact_url))
