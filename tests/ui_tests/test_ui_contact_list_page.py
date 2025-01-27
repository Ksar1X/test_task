from _pytest.fixtures import fixture
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from api_clients.user_client.models.requests.user import User
from tests.singleton import WebDriverSingleton
from tests.test_base_ui import TestBaseUi


class TestUIContactListPage(TestBaseUi):

    @fixture(scope="function", autouse=True)
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

    @staticmethod
    def refresh_browser():
        WebDriverSingleton.get_driver().refresh()
        WebDriverSingleton.wait_for_element(By.CLASS_NAME, 'contactTableBodyRow', EC.visibility_of_element_located)

    def test_add_new_contact(self, create_contact_fixture):
        contact = create_contact_fixture
        self.contact_list_page.add_contact()
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.add_contact_page.add_new_contact(contact)
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_cannot_add_contact_without_first_name_field(self, create_contact_fixture):
        contact = create_contact_fixture
        contact.firstName = ""
        self.contact_list_page.add_contact()
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.add_contact_page.add_new_contact(contact)
        self.base_page.assert_error_message('Contact validation failed: firstName: Path `firstName` is required.')

    def test_cannot_add_contact_without_last_name_field(self, create_contact_fixture):
        contact = create_contact_fixture
        contact.lastName = ""
        self.contact_list_page.add_contact()
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.add_contact_page.add_new_contact(contact)
        self.base_page.assert_error_message('Contact validation failed: lastName: Path `lastName` is required.')

    def test_edit_first_name_field(self, create_contact_fixture):
        contact = create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.update_field('first_name', 'Random')
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.contact_details_page.return_to_contact_list_page()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_edit_last_name_field(self, create_contact_fixture):
        contact = create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_last_name_field("Random")
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.contact_details_page.return_to_contact_list_page()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_edit_email_field(self, create_contact_fixture):
        contact = create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_email_field("fake@gmail.com")
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.contact_details_page.return_to_contact_list_page()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_edit_birthday_field(self, create_contact_fixture):
        contact = create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_birth_date_field("2004-01-10")
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.contact_details_page.return_to_contact_list_page()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_edit_phone_field(self, create_contact_fixture):
        contact = create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_phone_field("87654321")
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.contact_details_page.return_to_contact_list_page()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_edit_street1_field(self, create_contact_fixture):
        contact = create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_street1_field("fake")
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.contact_details_page.return_to_contact_list_page()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_edit_street2_field(self, create_contact_fixture):
        contact = create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_street2_field("fake")
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.contact_details_page.return_to_contact_list_page()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_edit_city_field(self, create_contact_fixture):
        contact = create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_city_field("fake")
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.contact_details_page.return_to_contact_list_page()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_edit_postal_field(self, create_contact_fixture):
        contact = create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_postal_code_field("12345")
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.contact_details_page.return_to_contact_list_page()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_edit_country_field(self, create_contact_fixture):
        contact = create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.go_to_edit_contact_page()
        self.edit_contact_page.change_country_field("FAKE")
        self.base_page.assert_url_changed(self.base_page.contact_url, self.base_page.add_contact_url)
        self.contact_details_page.return_to_contact_list_page()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)

    def test_delete_contact(self, create_contact_fixture):
        contact = create_contact_fixture
        self.refresh_browser()
        self.contact_list_page.click_on_contact(contact.email)
        self.contact_details_page.delete_contact()
        self.base_page.assert_url_changed(self.base_page.add_contact_url, self.base_page.contact_url)