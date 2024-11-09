import requests
from _pytest.fixtures import fixture

from api_clients.contacts_client.models.requests.create_contact_model import CreateContact
from api_clients.user_client.models.requests.user import User

class TestAddContact:
    url = "https://thinking-tester-contact-list.herokuapp.com/users"
    url_login = 'https://thinking-tester-contact-list.herokuapp.com/users/login'
    url_profile = "https://thinking-tester-contact-list.herokuapp.com/users/me"
    url_contacts = "https://thinking-tester-contact-list.herokuapp.com/contacts"



    @fixture(scope='class')
    def user_get_token_fixture(self):
        payload = User(email='garynych@gmail.com', password='raketa123').model_dump_json()
        response = requests.post(url=self.url_login, data=payload, headers={'Content-Type': 'application/json'})

        yield response.json().get('token')


    @fixture(scope='class')
    def create_contact(self, user_get_token_fixture):
        token = user_get_token_fixture
        payload = CreateContact(firstName="Joe1", lastName="Doe1", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE",
                                owner="").model_dump_json()
        response = requests.post(url=self.url_contacts, data=payload,
                                 headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'})
        id = response.json().get('_id')
        yield id


    def test_cannot_create_contact_without_login(self):
        payload = CreateContact(firstName="Joe", lastName="Doe", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE",
                                owner="").model_dump_json()
        response = requests.post(url=self.url_contacts, data=payload, headers={'Content-Type': 'application/json'})
        assert response.status_code == 401

    def test_cannot_add_contact_without_firstName_field(self, user_get_token_fixture):
        payload = CreateContact(firstName="", lastName="Doe", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE",
                                owner="6085a21efcfc72405667c3d4").model_dump_json()
        token = user_get_token_fixture
        response = requests.post(url=self.url_contacts, data=payload, headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'})
        assert response.status_code == 400

    def test_cannot_add_contact_without_lastName_field(self, user_get_token_fixture):
        payload = CreateContact(firstName="Joe", lastName="", birthdate="1999-10-10", email="joedoe@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE",
                                owner="6085a21efcfc72405667c3d4").model_dump_json()
        token = user_get_token_fixture
        response = requests.post(url=self.url_contacts, data=payload, headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'})
        assert response.status_code == 400

    def test_add_contact(self, user_get_token_fixture):
        token = user_get_token_fixture
        payload = CreateContact(firstName="Joe1", lastName="Doe", birthdate="1999-10-10", email="joedoe12341341341@fakemail.com",
                                phone="503645570", street1="fake", street2="fake",
                                city="fake", stateProvince="KS", postalCode="12345", country="FAKE",
                                owner="").model_dump_json()
        response = requests.post(url=self.url_contacts, data=payload,
                                 headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'})

        assert response.status_code == 201

    def test_delete_contact(self, user_get_token_fixture, create_contact):
        token = user_get_token_fixture
        id = create_contact
        url = self.url_contacts + f'/{id}'
        response = requests.delete(url=url, headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'})

        assert response.status_code == 200
        assert response.text == 'Contact deleted'

    def

