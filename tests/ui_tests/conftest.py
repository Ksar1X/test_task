import pytest

from api_clients.user_client.models.requests.user import User
from tests.test_base_ui import TestBaseUi
from tests.webdriver_singleton import WebDriverSingleton

test_base_ui = TestBaseUi()

@pytest.fixture(autouse=True)
def open_and_close_browser_fixture():
    WebDriverSingleton.get_driver()
    WebDriverSingleton.get_driver().get(test_base_ui.base_page.base_url)
    yield
    WebDriverSingleton.quit_driver()

@pytest.fixture()
def login_user_and_create_contact_fixture():
    user = test_base_ui.random_user.generate()
    test_base_ui.user_client.add_user(user=user)
    user = User(email=user.email, password=user.password)
    test_base_ui.login_page.login(user)
    response = test_base_ui.user_client.login_user(user)
    contact = test_base_ui.random_contact.generate()
    test_base_ui.contact_client.add_contact(data=contact, token=response.json().get('token'))
    yield contact
    test_base_ui.user_client.delete_user(token=response.json().get('token'))