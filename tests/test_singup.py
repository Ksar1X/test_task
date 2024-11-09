

from pytest import fixture

from api_clients.user_client.models.requests.create_user_model import CreateUser
from api_clients.user_client.user_client import add_user, get_user_profile, update_user, delete_user, login_user
from generators.user_generator import UserGenerator


class TestSignUp:

    @fixture(scope='class')
    def create_user_fixture(self):
        user = UserGenerator.generate()
        usercreted = add_user(user)
        yield usercreted.json().get("user").get("_id"), user.json().get('token')

    @staticmethod
    def delete_user_func(self, response):
        resp =  delete_user(response.json().get('user').get('_id'), response.json().get('token'))
        assert resp.status_code == 200


    def test_create_user_with_valid_fields(self, delete_user_func):
        payload = CreateUser(firstName="Joe", lastName="Doe", email="joedoe123312@gmail.com",password="joedoe123")
        response = add_user(payload)
        assert response.status_code == 201


    @fixture(scope='class')
    def create_and_delete_fixture(self):
        user = UserGenerator.generate()
        profile = add_user(user)
        yield profile
        response = delete_user(profile.json().get('_id'), profile.token)


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

    def test_get_user_profile(self):
        payload = CreateUser(firstName="Joe1", lastName="Doe1", email="joedoe@gmail.com",password="joedoe1234")
        response = add_user(payload)
        response = get_user_profile(response.json().get('_id'), response.json().get('token'))
        assert response.status_code == 200

    def test_update_user_profile(self):
        payload = CreateUser(firstName="Joe1", lastName="Doe1", email="joedoe@gmail.com",password="joedoe1234")
        response = add_user(payload)
        response = update_user(response.json().get('_id'), response.json().get('token'))
        assert response.status_code == 200


    def test_cannot_delete_user_without_login(self, create_and_login_fixture):
        user_id, token = create_and_login_fixture
        response = delete_user(user_id, None)
        assert response.status_code == 401
        assert response.json().get('token') is None

    def test_delete_user(self,create_and_login_fixture):
        user_id, token = create_and_login_fixture
        response = delete_user(user_id, token)
        assert response.status_code == 201



