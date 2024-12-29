import time

from _pytest.fixtures import fixture

from api_clients.contact_client.models.requests.create_contact_model import CreateContact
from api_clients.user_client.models.requests.user import User

from selenium.webdriver.support import expected_conditions as EC

from tests.test_base_ui import BaseUiTest


class TestUIContactListPage(BaseUiTest):

    @fixture(scope="class")
    def login_user_fixture(self):
        user = User(email="garynychxxx@gmail.com", password="raketa123")
        response = self.user_client.login_user(user)
        yield response, user
        self.driver.quit()


    def test_delete_contact(self, login_user_fixture):
        response, user = login_user_fixture

        contact = self.random_contact.generate()

        resp = self.contact_client.add_contact(data=contact, token=response.json().get('token'))
        contact_id = resp.json().get('_id')
        contact_list = self.contact_client.get_contact_list(token=response.json().get('token'))

        self.login_page.login(user)
        time.sleep(3)
        self.contact_list_page.delete_contact()
        time.sleep(3)
        self.contact_page.click_on_delete_button()

        assert contact_id not in contact_list

