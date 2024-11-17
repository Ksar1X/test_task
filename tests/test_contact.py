from _pytest.fixtures import fixture

from api_clients.api_clients_base import ApiClientBase, token_header
from api_clients.contact_client.contact_client import add_contact, delete_contact, get_contact, get_contact_list, \
    update_contact, put_contact, headers
from api_clients.contact_client.models.requests.create_contact_model import CreateContact

from api_clients.user_client.models.requests.user import User



class TestContact:

    @fixture(scope='class')
    def user_get_token_headers_fixture(self):
        payload = User(email='garynychxxx@gmail.com', password='raketa123')
        response = ApiClientBase.post_req(data=payload, postfix_url='/users/login')
        token_header['Authorization'] = f'Bearer {response.json().get('token')}'

        yield token_header



    @fixture(scope='class')
    def create_contact(self, user_get_token_headers_fixture):
        header = user_get_token_headers_fixture
        payload = CreateContact(firstName="Joe1", lastName="Doe1", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        response = ApiClientBase.post_req(data=payload, postfix_url='/contacts',token=header)
        indicator = response.json().get('_id')
        yield indicator, tken


    def test_cannot_create_contact_without_login(self):
        payload = CreateContact(firstName="Joe", lastName="Doe", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        response = ApiClientBase.post_req(data=payload, postfix_url='/contacts',token=token_header)
        assert response.status_code == 401

    def test_cannot_add_contact_without_firstName_field(self, user_get_token_fixture):
        payload = CreateContact(firstName="", lastName="Doe", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        token = user_get_token_fixture
        response = ApiClientBase.post_req(data=payload, postfix_url='/contacts',token=token_header)
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

    def test_get_contact(self, create_contact):
        indicator, token = create_contact
        response = get_contact(indicator, token)
        print(response)
        assert response.status_code == 200

    def test_get_contact_list(self, user_get_token_fixture):
        token = user_get_token_fixture
        response = get_contact_list(token)
        assert response.status_code == 200

    def test_change_contact_fields(self, create_contact):
        indicator, token = create_contact
        payload = CreateContact(firstName="Joe13", lastName="Doe2", birthdate="1999-10-10",
                                email="joedoe1231241341341@fakemail.com",
                                phone="503645530", street1="1fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE")
        response = put_contact(indicator, token, payload)
        assert response.status_code == 200
        response = get_contact(indicator, token)
        assert response.status_code == 200
        assert CreateContact(**response.json()) == payload

    def test_change_contact_field(self, create_contact):
        indicator, token = create_contact
        field_to_update = '{\"firstName\":\"asdasdasd\"}'
        response = update_contact(indicator, token, field_to_update)
        assert response.status_code == 200
        response = get_contact(indicator, token)
        assert response.status_code == 200
        assert response.json().get('firstName') == "asdasdasd"

    def test_delete_contact(self, create_contact):
        indicator, token = create_contact
        response = delete_contact(indicator, token)
        print(response)
        assert response.status_code == 200
        assert response.text == 'Contact deleted'





