from _pytest.fixtures import fixture

from Generators.generate_contact import ContactGenerator
from api_clients.contact_client.contact_client import ContactClient
from api_clients.contact_client.models.requests.create_contact_model import CreateContact
from api_clients.user_client.models.requests.user import User
from api_clients.user_client.user_client import UserClient

user_token_header = dict()

class TestContact:

    contact_client = ContactClient()
    user_client = UserClient()
    generate_contact = ContactGenerator()

    @fixture(scope='class')
    def user_get_token_fixture(self):
        user = User(email='garynychxxx@gmail.com', password='raketa123')
        response = self.user_client.login_user(user=user)
        yield response.json().get('token')



    @fixture(scope='class')
    def create_contact(self):
        contact = self.generate_contact.generate()
        response = self.user_client.login_user(user=User(email='garynychxxx@gmail.com', password='raketa123'))
        response = self.contact_client.add_contact(data=contact, token=response.json().get('token'))
        identification = response.json().get('_id')
        yield identification


    def test_cannot_create_contact_without_login(self, user_get_token_fixture):
        contact = CreateContact(firstName="Joe", lastName="Doe", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        response = self.contact_client.add_contact(data=contact, token='')
        assert response.status_code == 401

    def test_cannot_add_contact_without_firstname_field(self, user_get_token_fixture):
        contact = CreateContact(firstName="", lastName="Doe", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")

        response = self.contact_client.add_contact(data=contact, token=user_get_token_fixture)
        assert response.status_code == 400

    def test_cannot_add_contact_without_lastname_field(self, user_get_token_fixture):
        contact = CreateContact(firstName="Joe", lastName="", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        response = self.contact_client.add_contact(data=contact, token=user_get_token_fixture)
        assert response.status_code == 400

    def test_add_contact(self, user_get_token_fixture):
        contact = CreateContact(firstName="Joe1", lastName="Doe", birthdate="1999-10-10", email="joedoe12341341341@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        response = self.contact_client.add_contact(data=contact, token=user_get_token_fixture)
        assert response.status_code == 201

    def test_get_contact(self, create_contact, user_get_token_fixture):
         response = self.contact_client.get_contact(contact_id=create_contact, token=user_get_token_fixture)
         assert response.status_code == 200

    def test_get_contact_list(self, user_get_token_fixture):
         response = self.contact_client.get_contact_list(token=user_get_token_fixture)
         assert response.status_code == 200

    def test_change_contact_field(self, create_contact, user_get_token_fixture):
         field_to_update = '{\"firstName\":\"asdasdasd\"}'
         response = self.contact_client.update_contact(contact_id=create_contact, token=user_get_token_fixture, data=field_to_update)
         assert response.status_code == 200
         response = self.contact_client.get_contact(contact_id=create_contact, token=user_get_token_fixture)
         assert response.status_code == 200
         assert response.json().get('firstName') == "asdasdasd"

    def test_delete_contact(self, create_contact, user_get_token_fixture):
         response = self.contact_client.delete_contact(contact_id=create_contact, token=user_get_token_fixture)
         assert response.status_code == 200
         assert response.text == 'Contact deleted'





