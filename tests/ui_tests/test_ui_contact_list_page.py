import time
from _pytest.fixtures import fixture
from selenium.webdriver.support import expected_conditions as EC
from api_clients.user_client.models.requests.user import User
from tests.test_base_ui import TestBaseUi


class TestUIContactListPage(TestBaseUi):


    @fixture(scope="class")
    def login_user_fixture(self):
        user = User(email="garynychxxx@gmail.com", password="raketa123")
        self.login_page.login(email=user.email, password=user.password)
        response = self.user_client.login_user(user)
        yield response
        self.base_page.driver.quit()


    def test_delete_contact(self, login_user_fixture):
        response = login_user_fixture
        contact = self.random_contact.generate()
        self.contact_client.add_contact(data=contact,token=response.json().get('token'))
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.delete_contact()
        assert self.base_page.wait.until(EC.url_contains(self.base_page.contact_url))

    def test_add_new_contact(self, login_user_fixture):
        response = login_user_fixture
        contact = self.random_contact.generate()
        self.contact_list_page.add_contact()
        self.add_contact_page.add_new_contact(contact)
        assert self.base_page.wait.until(EC.url_contains(self.base_page.contact_url))


    def test_cannot_add_new_contact_without_fields(self, login_user_fixture):
        response = login_user_fixture
        contact = self.random_contact.generate()
        contact.firstName = ""
        contact.lastName = ""
        self.contact_list_page.add_contact()
        self.add_contact_page.add_new_contact(contact)
        error = self.add_contact_page.error()
        assert error is not None

    def test_edit_first_name_contact(self, login_user_fixture):
        response = login_user_fixture
        contact = self.random_contact.generate()
        self.contact_client.add_contact(data=contact, token=response.json().get('token'))
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact()
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_first_name_field("Random")
        self.edit_contact_page.click_on_submit_button()
        time.sleep(1)
        assert self.base_page.wait.until(EC.url_contains(self.base_page.contact_details_url))



