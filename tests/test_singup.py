from asyncio import AbstractEventLoopPolicy
from http.client import responses

from pytest import fixture

from GenerationUser.generate_unregistered_user import GenerateUser
from api_clients.user_client.user_client import *
from api_clients.api_clients_base import ApiClientBase

token_header = dict()




class TestSignUp:

    api = ApiClientBase()
    @fixture(scope='class')
    def create_user(self):
        user = GenerateUser().generate()
        yield user

    @fixture(scope="class")
    def delete_user_fixture(self):
        user = GenerateUser.generate()
        yield user
        profile = User(email=user.email, password=user.password)
        response = ApiClientBase.post_req(data=profile, postfix_url='/users/login')
        token_header['Authorization'] = f'Bearer {response.json().get('token')}'
        res = ApiClientBase.delete_req(postfix_url='/users/me', token=token_header)
        assert res.status_code == 200

    def test_create_user_with_valid_fields(self, delete_user_fixture):
        user = delete_user_fixture
        response = ApiClientBase.post_req(data=user, postfix_url='/users')
        assert response.status_code == 201

    def test_cannot_create_with_empty_fields(self):
        payload = CreateUser(firstName="", lastName="", email="", password="")
        response = ApiClientBase.post_req(data=payload, postfix_url='/users')
        assert response.status_code == 400

    def test_create_user_with_incorrect_email_field(self):
        payload = CreateUser(firstName="Joe", lastName="Doe", email="joedoe",password="joedoe123")
        response = ApiClientBase.post_req(data=payload, postfix_url='/users')
        assert response.status_code == 400
        assert response.json().get('message') == 'User validation failed: email: Email is invalid'

    def test_create_user_with_incorrect_pas_field(self):
        payload = CreateUser(firstName="Joe", lastName="Doe", email="joedoe@gmail.com",password="q")
        response = ApiClientBase.post_req(data=payload, postfix_url='/users')
        assert response.status_code == 400
        assert response.json().get('message') == 'User validation failed: password: Path `password` (`q`) is shorter than the minimum allowed length (7).'

    def test_cannot_create_registered_user(self):
        payload = CreateUser(firstName="Joe1", lastName="Doe1", email="joedoe@gmail.com",password="joedoe1234")
        response = ApiClientBase.post_req(data=payload, postfix_url='/users')
        assert response.status_code == 400
        assert response.json().get('message') == 'Email address is already in use'


    def test_cannot_delete_user_without_login(self):
        user = GenerateUser().generate()
        profile = User(email=user.email, password=user.password)
        response = ApiClientBase.delete_req(postfix_url='/users/me', token=token_header)
        assert response.status_code == 401

    def test_delete_user(self, create_user):
        user = create_user
        response = ApiClientBase.post_req(data=user, postfix_url='/users')
        token_header['Authorization'] = f'Bearer {response.json().get('token')}'
        res = ApiClientBase.delete_req(postfix_url='/users/me', token=token_header)
        assert res.status_code == 200


    def test_update_user(self, delete_user_fixture):
        user = delete_user_fixture
        res = ApiClientBase.post_req(data=user, postfix_url='/users')
        token_header['Authorization'] = f'Bearer {res.json().get('token')}'
        profile = User(email=user.email, password=user.password)
        response = ApiClientBase.patch_req(data=profile, postfix_url='/users/me', token=token_header)
        assert response.status_code == 200

    def test_get_user_profile(self, delete_user_fixture):
        user = delete_user_fixture
        res = ApiClientBase.post_req(data=user, postfix_url='/users')
        token_header['Authorization'] = f'Bearer {res.json().get('token')}'
        response = ApiClientBase.get_req(postfix_url='/users/me', token = token_header)
        print(response)
        assert response.status_code == 200

