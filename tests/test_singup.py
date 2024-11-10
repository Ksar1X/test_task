from http.client import responses

from pytest import fixture
import requests

from api_clients.user_client import user_client
from api_clients.user_client.models.requests.create_user_model import CreateUser
from api_clients.user_client.user_client import add_user, login_user


class TestSignUp:

    url = "https://thinking-tester-contact-list.herokuapp.com/users"
    url_login = 'https://thinking-tester-contact-list.herokuapp.com/users/login'
    url_profile = "https://thinking-tester-contact-list.herokuapp.com/users/me"

    @fixture(scope="class")
    def create_and_login_fixture(self):
        payload = CreateUser(firstName="E", lastName="G",email="garynychxxx@gmail.com", password="raketa123").model_dump_json()
        requests.post(url=self.url, data=payload, headers={'Content-Type': 'application/json'})
        response = requests.post(url=self.url_login, data=payload, headers={'Content-Type': 'application/json'})
        assert response.status_code == 200

        yield response.json().get('token')


    @fixture(scope="class")
    def delete_user_fixture(self):
        user = CreateUser(firstName="Joe1", lastName="Doe", email="joedoe3233@gmail.com", password="joedoe123")
        yield user
        response = requests.post(url=self.url_login, data=user.model_dump_json(), headers={'Content-Type': 'application/json'})
        requests.delete(url= self.url_profile, headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {response.json().get("token")}'})

    def test_create_user_with_valid_fields(self, delete_user_fixture):
        user = delete_user_fixture
        response = add_user(user)
        assert response.status_code == 201

    def test_create_user_with_incorrect_email_field(self):
        payload = CreateUser(firstName="Joe", lastName="Doe", email="joedoe",password="joedoe123")
        response = add_user(payload)
        assert response.status_code == 400
        assert response.json().get('message') == 'User validation failed: email: Email is invalid'

    def test_create_user_with_incorrect_pas_field(self):
        payload = CreateUser(firstName="Joe", lastName="Doe", email="joedoe@gmail.com",password="q")
        response = add_user(payload)
        assert response.status_code == 400
        assert response.json().get('message') == 'User validation failed: password: Path `password` (`q`) is shorter than the minimum allowed length (7).'

    def test_cannot_create_registered_user(self):
        payload = CreateUser(firstName="Joe1", lastName="Doe1", email="joedoe@gmail.com",password="joedoe1234")
        response = add_user(payload)
        assert response.status_code == 400
        assert response.json().get('message') == 'Email address is already in use'

















    def test_cannot_delete_user_without_login(self):
        response = requests.delete(url= self.url_profile, headers={'Content-Type': 'application/json'})
        assert response.status_code == 401

    def test_delete_user(self, delete_user_fixture):
        user = delete_user_fixture
        response = login_user(user)
        response = user_client.delete_user(user, response.json().get('token'))
        assert response.status_code == 200


