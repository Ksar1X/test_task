import time
from _pytest.fixtures import fixture
from selenium.webdriver.support import expected_conditions as EC
from api_clients.user_client.models.requests.user import User
from tests.singleton import WebDriverSingleton
from tests.test_base_ui import TestBaseUi


class TestUIContactListPage(TestBaseUi):

    @fixture
    def open_and_close_browser_fixture(self):
        WebDriverSingleton.get_driver()
        WebDriverSingleton.get_driver().get(self.base_page.base_url)
        yield
        WebDriverSingleton.quit_driver()

    @fixture
    def login_user_fixture(self):
        user = self.random_user.generate()
        self.user_client.add_user(user=user)
        user = User(email=user.email, password=user.password)
        self.login_page.login(user)
        response = self.user_client.login_user(user)
        yield response

    @fixture
    def create_contact_fixture(self, login_user_fixture):
        response = login_user_fixture
        contact = self.random_contact.generate()
        self.contact_client.add_contact(data=contact, token=response.json().get('token'))
        yield contact

    def test_add_new_contact(self, open_and_close_browser_fixture, create_contact_fixture):
        time.sleep(1)
        self.contact_list_page.add_contact()
        contact = create_contact_fixture
        time.sleep(1)
        self.add_contact_page.add_new_contact(contact)
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), "New contact successfully created!"


    def test_cannot_add_contact_without_first_name_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        contact.firstName = ""
        time.sleep(1)
        self.contact_list_page.add_contact()
        time.sleep(1)
        self.add_contact_page.add_new_contact(contact)
        time.sleep(1)
        error = self.add_contact_page.error()
        assert error == 'Contact validation failed: firstName: Path `firstName` is required.'

    def test_cannot_add_contact_without_last_name_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        contact.lastName = ""
        time.sleep(3)
        self.contact_list_page.add_contact()
        time.sleep(3)
        self.add_contact_page.add_new_contact(contact)
        time.sleep(3)
        error = self.add_contact_page.error()
        assert error == 'Contact validation failed: lastName: Path `lastName` is required.'

    def test_edit_first_name_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_first_name_field("Random")
        time.sleep(1)
        self.contact_details_page.return_to_contact_list_page()
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), 'First Name field successfully changed!'

    def test_edit_last_name_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_last_name_field("Random")
        time.sleep(1)
        self.contact_details_page.return_to_contact_list_page()
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), 'Last Name field successfully changed!'

    def test_edit_email_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_email_field("fake@gmail.com")
        time.sleep(1)
        self.contact_details_page.return_to_contact_list_page()
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), 'Email field successfully changed!'

    def test_edit_birthday_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_birth_date_field("2004-01-10")
        time.sleep(1)
        self.contact_details_page.return_to_contact_list_page()
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), 'Birthday field successfully changed!'

    def test_edit_phone_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_phone_field("87654321")
        time.sleep(1)
        self.contact_details_page.return_to_contact_list_page()
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), 'Phone field successfully changed!'

    def test_edit_street1_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_street1_field("fake")
        time.sleep(1)
        self.contact_details_page.return_to_contact_list_page()
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), 'Street1 field successfully changed!'

    def test_edit_street2_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_street2_field("fake")
        time.sleep(1)
        self.contact_details_page.return_to_contact_list_page()
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), 'Street2 field successfully changed!'

    def test_edit_city_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_city_field("fake")
        time.sleep(1)
        self.contact_details_page.return_to_contact_list_page()
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), 'City field successfully changed!'

    def test_edit_postal_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_postal_code_field("12345")
        time.sleep(1)
        self.contact_details_page.return_to_contact_list_page()
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), 'Postal code field successfully changed!'

    def test_edit_country_field(self, open_and_close_browser_fixture, create_contact_fixture):
        contact = create_contact_fixture
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_country_field("FAKE")
        time.sleep(1)
        self.contact_details_page.return_to_contact_list_page()
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), 'Postal code field successfully changed!'

    def test_delete_contact(self, open_and_close_browser_fixture, login_user_fixture):
        response = login_user_fixture
        contact = self.random_contact.generate()
        self.contact_client.add_contact(data=contact,token=response.json().get('token'))
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.delete_contact()
        assert WebDriverSingleton.wait_for_element(self.base_page.add_contact_url, self.base_page.contact_url, EC.url_changes), "Contact successfully deleted!"