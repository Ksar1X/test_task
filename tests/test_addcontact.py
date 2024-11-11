from _pytest.fixtures import fixture

from api_clients.contact_client.contact_client import add_contact, delete_contact, get_contact, get_contact_list
from api_clients.contact_client.models.create_contact_model import CreateContact
from api_clients.user_client.models.requests.user import User
from api_clients.user_client.user_client import login_user


class TestAddContact:

    @fixture(scope='class')
    def user_get_token_fixture(self):
        payload = User(email='garynychxxx@gmail.com', password='raketa123')
        response = login_user(payload)
        print(response)

        yield response.json().get('token')



    @fixture(scope='class')
    def create_contact(self, user_get_token_fixture):
        token = user_get_token_fixture
        payload = CreateContact(firstName="Joe1", lastName="Doe1", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        response = add_contact(payload, token)
        indicator = response.json().get('_id')
        yield indicator


    def test_cannot_create_contact_without_login(self):
        payload = CreateContact(firstName="Joe", lastName="Doe", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        response = add_contact(payload, "")
        assert response.status_code == 401

    def test_cannot_add_contact_without_firstName_field(self, user_get_token_fixture):
        payload = CreateContact(firstName="", lastName="Doe", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        token = user_get_token_fixture
        response = add_contact(payload, token)
        assert response.status_code == 400

    def test_cannot_add_contact_without_lastName_field(self, user_get_token_fixture):
        payload = CreateContact(firstName="Joe", lastName="", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        token = user_get_token_fixture
        response = add_contact(payload, token)
        assert response.status_code == 400

    def test_add_contact(self, user_get_token_fixture):
        token = user_get_token_fixture
        payload = CreateContact(firstName="Joe1", lastName="Doe", birthdate="1999-10-10", email="joedoe12341341341@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        response = add_contact(payload, token)

        assert response.status_code == 201

    def test_delete_contact(self, user_get_token_fixture, create_contact):
        token = user_get_token_fixture
        indicator = create_contact
        response = delete_contact(token, indicator)

        assert response.status_code == 200
        assert response.text == 'Contact deleted'

    def test_get_contact(self, user_get_token_fixture, create_contact):
        token = user_get_token_fixture
        indicator = create_contact
        response = get_contact(indicator, token)
        assert response.status_code == 200

    def test_get_contact_list(self, user_get_token_fixture):
        token = user_get_token_fixture
        response = get_contact_list(token)
        assert response.status_code == 200




