from pytest import fixture
import requests

from models.create_user_model import CreateUser
from models.user import User

class TestSignUp:

    url = "https://thinking-tester-contact-list.herokuapp.com/users"
    url_login = 'https://thinking-tester-contact-list.herokuapp.com/users/login'
    url_delete = "https://thinking-tester-contact-list.herokuapp.com/users/me"

    global user


    @fixture(scope="class")
    def delete_user_fixture(self):
        yield
        payload = User(email=user.email, password=user.password).model_dump_json()
        response = requests.post(url=self.url_login, data=payload, headers={'Content-Type': 'application/json'})
        token = response.json().get('token')
        assert response.status_code == 200

    @fixture(scope="class")
    def login_user_fixture(self):
        yield
        payload = User(email=user.email, password=user.password).model_dump_json()
        response = requests.post(url=self.url_login, data=payload, headers={'Content-Type': 'application/json'})
        token = response.json().get('token')
        response = requests.delete(url=self.url_delete,headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'})
        assert response.status_code == 200


    def test_create_user_with_valid_fields(self, login_user_fixture, delete_user_fixture):
        payload = CreateUser(firstName="Joe", lastName="Doe", email="joedoe@gmail.com", password="joedoe123")
        global user
        user = payload
        response = requests.post(url= self.url, data=payload.model_dump_json(), headers={'Content-Type': 'application/json'})
        assert response.status_code == 201

    def test_create_user_with_incorrect_email_field(self):
        payload = CreateUser(firstName="Joe", lastName="Doe", email="joedoe",password="joedoe123").model_dump_json()
        response = requests.post(url=self.url, data=payload, headers={'Content-Type': 'application/json'})
        assert response.status_code == 400
        assert response.json().get('message') == 'User validation failed: email: Email is invalid'

    def test_create_user_with_incorrect_pas_field(self):
        payload = CreateUser(firstName="Joe", lastName="Doe", email="joedoe@gmail.com",password="q").model_dump_json()
        response = requests.post(url=self.url, data=payload, headers={'Content-Type': 'application/json'})
        assert response.status_code == 400
        assert response.json().get('message') == 'User validation failed: password: Path `password` (`q`) is shorter than the minimum allowed length (7).'

    def test_cannot_create_registered_user(self):
        payload = CreateUser(firstName="Joe1", lastName="Doe1", email="joedoe@gmail.com",password="joedoe1234").model_dump_json()
        response = requests.post(url=self.url, data=payload, headers={'Content-Type': 'application/json'})
        assert response.status_code == 400
        assert response.json().get('message') == 'Email address is already in use'
