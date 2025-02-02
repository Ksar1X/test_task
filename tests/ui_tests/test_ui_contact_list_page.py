from _pytest.fixtures import fixture
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from api_clients.user_client.models.requests.user import User
from tests.webdriver_singleton import WebDriverSingleton
from tests.test_base_ui import TestBaseUi


class TestUIContactListPage(TestBaseUi):

    @fixture(scope="function", autouse=True)
    def open_and_close_browser_fixture(self):
        WebDriverSingleton.get_driver()
        WebDriverSingleton.get_driver().get(self.base_page.base_url)
        yield
        WebDriverSingleton.quit_driver()

    @fixture
    def login_user_and_create_contact_fixture(self):
        user = self.random_user.generate()
        self.user_client.add_user(user=user)
        user = User(email=user.email, password=user.password)
        self.login_page.login(user)
        response = self.user_client.login_user(user)
        contact = self.random_contact.generate()
        self.contact_client.add_contact(data=contact, token=response.json().get('token'))
        yield contact
        self.user_client.delete_user(token=response.json().get('token'))

    @staticmethod
    def refresh_browser():
        WebDriverSingleton.get_driver().refresh()
        WebDriverSingleton.wait_for_element(By.CLASS_NAME, 'contactTableBodyRow', EC.visibility_of_element_located)

    def edit_contact(self, email, field: str, message: str):
        self.contact_list_page.click_on_contact(email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.update_field(field, message)
        self.base_page.assert_url_changed(self.base_page.edit_contact_url, self.base_page.contact_details_url)
        self.contact_details_page.return_to_contact_list_page()
        self.base_page.assert_url_changed(self.base_page.contact_details_url, self.base_page.contact_url)

    def test_add_new_contact(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.contact_list_page.add_contact()
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.add_contact_page.add_new_contact(contact)
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_cannot_add_contact_without_first_name_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        contact.firstName = ""
        self.contact_list_page.add_contact()
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.add_contact_page.add_new_contact(contact)
        self.base_page.assert_error_message('Contact validation failed: firstName: Path `firstName` is required.')

    def test_cannot_add_contact_without_last_name_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        contact.lastName = ""
        self.contact_list_page.add_contact()
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.add_contact_page.add_new_contact(contact)
        self.base_page.assert_error_message('Contact validation failed: lastName: Path `lastName` is required.')

    def test_edit_first_name_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.refresh_browser()
        self.edit_contact(contact.email, "first_name", "Random")

    def test_edit_last_name_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.refresh_browser()
        self.edit_contact(contact.email, "last_name", "Random")

    def test_edit_email_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.refresh_browser()
        self.edit_contact(contact.email, "email", "Random@gmail.com")

    def test_edit_birthday_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.refresh_browser()
        self.edit_contact(contact.email, "birthdate", "2000-01-01")

    def test_edit_phone_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.refresh_browser()
        self.edit_contact(contact.email, "phone", "12345678")

    def test_edit_street1_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.refresh_browser()
        self.edit_contact(contact.email, "street1", "Random")

    def test_edit_street2_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.refresh_browser()
        self.edit_contact(contact.email, "street2", "Random")

    def test_edit_city_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.refresh_browser()
        self.edit_contact(contact.email, "city", "Random")

    def test_edit_postal_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.refresh_browser()
        self.edit_contact(contact.email, "postal_code", "12345")

    def test_edit_country_field(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.refresh_browser()
        self.edit_contact(contact.email, "country", "Random")

    def test_delete_contact(self, login_user_and_create_contact_fixture):
        contact = login_user_and_create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.delete_contact()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)