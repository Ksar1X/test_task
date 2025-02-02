from api_clients.contact_client.models.requests.contact_field_model import ContactField
from tests.test_base import BaseTest

class TestContact(BaseTest):

    def test_cannot_create_contact_without_login(self):
        contact = self.random_contact.generate()
        response = self.contact_client.add_contact(data=contact, token='')
        assert response.status_code == 401

    def test_cannot_add_contact_without_firstname_field(self, user_get_token_fixture):
        contact = self.random_contact.generate()
        token, user = user_get_token_fixture
        contact.firstName = ""
        response = self.contact_client.add_contact(data=contact, token=token)
        assert response.status_code == 400

    def test_cannot_add_contact_without_lastname_field(self, user_get_token_fixture):
        contact = self.random_contact.generate()
        token, user = user_get_token_fixture
        contact.lastName = ""
        response = self.contact_client.add_contact(data=contact, token=token)
        assert response.status_code == 400

    def test_add_contact(self, user_get_token_fixture):
        contact = self.random_contact.generate()
        token, user = user_get_token_fixture
        response = self.contact_client.add_contact(data=contact, token=token)
        assert response.status_code == 201

    def test_get_contact(self, get_contact_id_fixture, user_get_token_fixture):
        token, user = user_get_token_fixture
        response = self.contact_client.get_contact(contact_id=get_contact_id_fixture, token=token)
        assert response.status_code == 200

    def test_get_contact_list(self, user_get_token_fixture):
        token, user = user_get_token_fixture
        response = self.contact_client.get_contact_list(token=token)
        assert response.status_code == 200

    def test_change_contact_field(self, get_contact_id_fixture, user_get_token_fixture):
        token, user = user_get_token_fixture
        response = self.contact_client.update_contact(contact_id=get_contact_id_fixture, token=token, data=ContactField(firstName="asdasdasd"))
        assert response.status_code == 200
        response = self.contact_client.get_contact(contact_id=get_contact_id_fixture, token=token)
        assert response.status_code == 200
        assert response.json().get('firstName') == "asdasdasd"

    def test_delete_contact(self, get_contact_id_fixture, user_get_token_fixture):
        token, user = user_get_token_fixture
        response = self.contact_client.delete_contact(contact_id=get_contact_id_fixture, token=token)
        assert response.status_code == 200
        assert response.text == 'Contact deleted'





