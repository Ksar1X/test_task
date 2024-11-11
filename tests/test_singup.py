from http.client import responses

from pytest import fixture
from api_clients.user_client.user_client import *

class TestSignUp:

    @fixture(scope='class')
    def create_user(self):
        user = GenerateUser().generate()
        yield user

    @fixture(scope="class")
    def delete_user_fixture(self):
        user = GenerateUser.generate()
        yield user
        profile = User(email=user.email, password=user.password)
        response = login_user(profile)
        res = delete_user(profile, response.json().get('token'))
        assert res.status_code == 200

    def test_create_user_with_valid_fields(self, delete_user_fixture):
        user = delete_user_fixture
        response = add_user(user)
        assert response.status_code == 201

    def test_cannot_create_with_empty_fields(self):
        payload = CreateUser(firstName="", lastName="", email="", password="")
        response = add_user(payload)
        assert response.status_code == 400

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
        user = GenerateUser().generate()
        profile = User(email=user.email, password=user.password)
        response = delete_user(profile, None)
        assert response.status_code == 401

    def test_delete_user(self, create_user):
        user = create_user
        response = add_user(user)
        profile = User(email=user.email, password=user.password)
        res = delete_user(profile, response.json().get('token'))
        assert res.status_code == 200


    def test_get_user_profile(self, delete_user_fixture):
        user = delete_user_fixture
        add_user(user)
        profile = User(email=user.email, password=user.password)
        res = login_user(profile)
        response = get_user_profile(res.json().get('user').get('_id'), res.json().get('token'))
        assert response.status_code == 200

    def test_update_user(self, delete_user_fixture):
        user = delete_user_fixture
        add_user(user)
        profile = User(email=user.email, password=user.password)
        res = login_user(profile)
        response = update_user(profile, res.json().get('token'))
        assert response.status_code == 200



