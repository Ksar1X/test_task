from _pytest.fixtures import fixture

from api_clients.user_client.models.requests.user import User
from api_clients.user_client.user_client import UserClient

user_token_header = dict()

class TestLogIn:

    @fixture(scope='class')
    def get_user_token(self):
        user = User(email="garynychxxx@gmail.com", password="q")
        response = UserClient.login_user(user=user)
        yield user, f'Bearer {response.json().get('token')}'

    def test_registered_user_able_login(self):
        user = User(email="garynych@gmail.com", password="raketa123")
        response = UserClient.login_user(user=user)
        assert response.status_code == 200
        assert response.json().get('token') is not None

    def test_unregistered_user_able_login(self):
        user = User(email="qwerrsfgsv@gmail.com", password="raketa1234")
        response = UserClient.login_user(user=user)
        assert response.status_code == 401

    def test_registered_user_with_incorrect_pas_cannot_login(self):
        user = User(email="garynychxxx@gmail.com", password="q")
        response = UserClient.login_user(user=user)
        assert response.status_code == 401

    def test_cannot_logout_without_login(self):
        user = User(email="garynychxxx@gmail.com", password="raketa1234")
        response = UserClient.login_user(user=user)
        assert response.status_code == 401

    def test_logout_user(self, get_user_token):
        user, user_token_header['Authorization'] = get_user_token
        response = UserClient.logout_user(user=user, token=user_token_header)
        assert response.status_code == 200

    def test_user_cannot_logout_without_login(self):
        user = User(email="garynychxxx@gmail.com", password="raketa123")
        response = UserClient.logout_user(user=user, token=None)
        assert response.status_code == 401
        assert response.json().get('token') is None






