from _pytest.fixtures import fixture
from api_clients.user_client.models.requests.create_user_model import CreateUser
from tests.singleton import WebDriverSingleton
from tests.test_base_ui import TestBaseUi


class TestUISingUpPage(TestBaseUi):

    @fixture(scope="function", autouse=True)
    def open_and_close_browser_fixture(self):
        WebDriverSingleton.get_driver()
        WebDriverSingleton.get_driver().get(self.base_page.sing_up_url)
        yield
        WebDriverSingleton.quit_driver()


    def test_user_cannot_create_without_empty_fields(self):
        self.singUp_page.create_user(CreateUser(email='', password='', lastName='', firstName=''))
        self.base_page.assert_error_message('User validation failed: firstName: Path `firstName` is required., lastName: Path `lastName` is required., email: Email is invalid, password: Path `password` is required.')


    def test_user_cannot_create_without_first_name_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password=user.password, lastName=user.lastName, firstName=''))
        self.base_page.assert_error_message('User validation failed: firstName: Path `firstName` is required.')


    def test_user_cannot_create_without_last_name_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password=user.password, lastName='', firstName=user.firstName))
        self.base_page.assert_error_message('User validation failed: lastName: Path `lastName` is required.')


    def test_user_cannot_create_without_email_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email='', password=user.password, lastName=user.lastName, firstName=user.firstName))
        self.base_page.assert_error_message('User validation failed: email: Email is invalid')


    def test_user_cannot_create_without_password_field(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password='', lastName=user.lastName, firstName=user.firstName))
        self.base_page.assert_error_message('User validation failed: password: Path `password` is required.')


    def test_sign_up(self):
        user = self.random_user.generate()
        self.singUp_page.create_user(CreateUser(email=user.email, password=user.password, lastName=user.lastName, firstName=user.firstName))
        self.base_page.assert_url_changed(self.base_page.sing_up_url, self.base_page.contact_url)
