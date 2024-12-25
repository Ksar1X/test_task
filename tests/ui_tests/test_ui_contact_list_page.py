import time

from _pytest.fixtures import fixture

from api_clients.contact_client.models.requests.create_contact_model import CreateContact
from api_clients.user_client.models.requests.user import User
from tests.test_base import BaseTest
from selenium.webdriver.support import expected_conditions as EC

class TestUIContactListPage(BaseTest):

    @fixture(scope="class")
    def login_user_fixture(self):
        user = User(email="garynychxxx@gmail.com", password="raketa123")
        self.login_page.login(user)
        response = self.user_client.login_user(user)
        yield response
        self.base_page.driver.quit()


    def test_delete_contact(self, login_user_fixture):
        response = login_user_fixture
        contact = self.random_contact.generate()
        self.contact_client.add_contact(data=contact,token=response.json().get('token'))
        ##self.contact_list_page.wait.until(EC.visibility_of_element_located(self.contact_list_page.CONTACT_ROW)) -- как это через ожидания сделать?????????
        self.base_page.driver.refresh()
        time.sleep(1)
        self.contact_list_page.delete_contact()
        self.contact_page.click_on_delete_button()
        contact_list = self.contact_client.get_contact_list(token=response.json().get('token'))
        assert contact.lastName not in contact_list

