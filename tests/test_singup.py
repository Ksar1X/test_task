from pytest import fixture
from Generate.generate_unregistered_user import GenerateUser
from api_clients.user_client.user_client import *
from api_clients.api_clients_base import ApiClientBase



user_token_header = dict()

class TestSignUp:

    @fixture(scope='class')
    def create_user(self):
        user = GenerateUser().generate()
        yield user

    @fixture(scope="class")
    def delete_user_fixture(self):
        user = GenerateUser.generate()
        yield user
        user = User(email=user.email, password=user.password)
        response = UserClient.login_user(user=user)
        user_token_header['Authorization'] = f'Bearer {response.json().get('token')}'
        response = UserClient.delete_user(user=user, token=user_token_header)
        assert response.status_code == 200

    def test_create_user_with_valid_fields(self, delete_user_fixture):
        user = delete_user_fixture
        response = UserClient.add_user(user=user)
        assert response.status_code == 201

    def test_cannot_create_with_empty_fields(self):
        user = CreateUser(firstName="", lastName="", email="", password="")
        response = UserClient.add_user(user=user)
        assert response.status_code == 400

    def test_create_user_with_incorrect_email_field(self):
        user = CreateUser(firstName="Joe", lastName="Doe", email="joedoe",password="joedoe123")
        response = UserClient.add_user(user=user)
        assert response.status_code == 400
        assert response.json().get('message') == 'User validation failed: email: Email is invalid'

    def test_create_user_with_incorrect_pas_field(self):
        user = CreateUser(firstName="Joe", lastName="Doe", email="joedoe@gmail.com",password="q")
        response = UserClient.add_user(user=user)
        assert response.status_code == 400
        assert response.json().get('message') == 'User validation failed: password: Path `password` (`q`) is shorter than the minimum allowed length (7).'

    def test_cannot_create_registered_user(self):
        user = CreateUser(firstName="Joe1", lastName="Doe1", email="joedoe@gmail.com",password="joedoe1234")
        response = UserClient.add_user(user=user)
        assert response.status_code == 400
        assert response.json().get('message') == 'Email address is already in use'


    def test_cannot_delete_user_without_login(self):
        user = GenerateUser().generate()
        user = User(email=user.email, password=user.password)
        response = UserClient.delete_user(user=user, token=None)
        assert response.status_code == 401

    def test_delete_user(self, create_user):
        user = create_user
        response = ApiClientBase.post_req(data=user, postfix_url='/users')
        user_token_header['Authorization'] = f'Bearer {response.json().get('token')}'
        res = UserClient.delete_user(user=user, token=user_token_header)
        assert res.status_code == 200


    def test_update_user(self, delete_user_fixture):
        user = delete_user_fixture
        response = UserClient.add_user(user=user)
        user_token_header['Authorization'] = f'Bearer {response.json().get('token')}'
        user = User(email=user.email, password=user.password)
        response = UserClient.update_user(user=user, token=user_token_header)
        assert response.status_code == 200

    def test_get_user_profile(self, delete_user_fixture):
        user = delete_user_fixture
        response = UserClient.add_user(user=user)
        user_token_header['Authorization'] = f'Bearer {response.json().get('token')}'
        response = UserClient.get_user_profile(token=user_token_header)
        assert response.status_code == 200

