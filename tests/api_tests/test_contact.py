from _pytest.fixtures import fixture
from api_clients.contact_client.models.requests.contact_field_model import ContactField
from api_clients.contact_client.models.requests.create_contact_model import CreateContact
from api_clients.user_client.models.requests.user import User
from tests.test_base import BaseTest

user_token_header = dict()

class TestContact(BaseTest):


    @fixture(scope='class')
    def create_user_fixture(self):
        user = self.random_user.generate()
        self.user_client.add_user(user=user)
        yield user

    @fixture(scope='class')
    def user_get_token_fixture(self, create_user_fixture):
        user = create_user_fixture
        response = self.user_client.login_user(user=User(email=user.email, password=user.password))
        yield response.json().get('token'), user



    @fixture(scope='class')
    def get_contact_id(self, user_get_token_fixture):
        token, user = user_get_token_fixture
        self.user_client.login_user(user=User(email=user.email, password=user.password))
        contact = self.random_contact.generate()
        response = self.contact_client.add_contact(data=contact, token=token)
        identification = response.json().get('_id')
        yield identification


    def test_cannot_create_contact_without_login(self, user_get_token_fixture):
        token, user = user_get_token_fixture
        contact = self.random_contact.generate()
        response = self.contact_client.add_contact(data=contact, token='')
        assert response.status_code == 401

    def test_cannot_add_contact_without_firstname_field(self, user_get_token_fixture):
        contact = self.random_contact.generate()
        token, user = user_get_token_fixture
        contact = CreateContact(firstName="", lastName=contact.lastName, birthdate=contact.birthdate, email=contact.email,
                                phone=contact.phone, street1=contact.street1, street2=contact.street2,
                                city=contact.city, stateProvince=contact.stateProvince, postalCode=contact.postalCode, country=contact.country)

        response = self.contact_client.add_contact(data=contact, token=token)
        assert response.status_code == 400

    def test_cannot_add_contact_without_lastname_field(self, user_get_token_fixture):
        contact = self.random_contact.generate()
        token, user = user_get_token_fixture
        contact = CreateContact(firstName=contact.firstName, lastName="", birthdate=contact.birthdate,
                                email=contact.email,
                                phone=contact.phone, street1=contact.street1, street2=contact.street2,
                                city=contact.city, stateProvince=contact.stateProvince, postalCode=contact.postalCode,
                                country=contact.country)
        response = self.contact_client.add_contact(data=contact, token=token)
        assert response.status_code == 400

    def test_add_contact(self, user_get_token_fixture):
        contact = self.random_contact.generate()
        token, user = user_get_token_fixture
        response = self.contact_client.add_contact(data=contact, token=token)
        assert response.status_code == 201

    def test_get_contact(self, get_contact_id, user_get_token_fixture):
        token, user = user_get_token_fixture
        response = self.contact_client.get_contact(contact_id=get_contact_id, token=token)
        assert response.status_code == 200

    def test_get_contact_list(self, user_get_token_fixture):
        token, user = user_get_token_fixture
        response = self.contact_client.get_contact_list(token=token)
        assert response.status_code == 200

    def test_change_contact_field(self, get_contact_id, user_get_token_fixture):
        token, user = user_get_token_fixture
        response = self.contact_client.update_contact(contact_id=get_contact_id, token=token, data=ContactField(firstName="asdasdasd"))
        assert response.status_code == 200
        response = self.contact_client.get_contact(contact_id=get_contact_id, token=token)
        assert response.status_code == 200
        assert response.json().get('firstName') == "asdasdasd"

    def test_delete_contact(self, get_contact_id, user_get_token_fixture):
        token, user = user_get_token_fixture
        response = self.contact_client.delete_contact(contact_id=get_contact_id, token=token)
        assert response.status_code == 200
        assert response.text == 'Contact deleted'





