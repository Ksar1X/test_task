from api_clients.contact_client.models.requests.create_contact_model import CreateContact
from tests.test_base import BaseTest
from selenium.webdriver.support import expected_conditions as EC

class TestUIContactListPage(BaseTest):

    def test_add_contact_to_contact_list(self):
        contact = self.random_contact.generate()
        self.contact_list_page.create_contact(CreateContact(firstName=contact.firstName, lastName=contact.lastName, birthdate=contact.birthdate, email=contact.email, phone=contact.phone, street1=contact.street1, street2=contact.street2, city=contact.city, stateProvince=contact.stateProvince, postalCode=contact.postalCode, country=contact.country))
        assert self.contact_list_page.wait.until(EC.url_changes(self.login_page.contact_url))
