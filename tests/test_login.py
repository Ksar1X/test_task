from _pytest.fixtures import fixture

from api_clients.user_client.models.requests.user import User
from api_clients.user_client.user_client import UserClient

class TestLogIn:
    user_client = UserClient()

    @fixture(scope='class')
    def get_user_token_fixture(self):
        user = User(email="garynychxxx@gmail.com", password="raketa123")
        response = self.user_client.login_user(user=user)
        token = response.json().get('token')
        print(token)
        yield user, token

    def test_registered_user_able_login(self):
        user = User(email="garynych@gmail.com", password="raketa123")
        response = self.user_client.login_user(user=user)
        assert response.status_code == 200
        assert response.json().get('token') is not None

    def test_unregistered_user_able_login(self):
        user = User(email="qwerrsfgsv@gmail.com", password="raketa1234")
        response = self.user_client.login_user(user=user)
        assert response.status_code == 401

    def test_registered_user_with_incorrect_pas_cannot_login(self):
        user = User(email="garynychxxx@gmail.com", password="q")
        response = self.user_client.login_user(user=user)
        assert response.status_code == 401

    def test_logout_user(self, get_user_token_fixture):
        user, user_token = get_user_token_fixture
        response = self.user_client.logout_user(user=user, token=user_token)
        assert response.status_code == 200

    def test_user_cannot_logout_without_login(self):
        user = User(email="garynychxxx@gmail.com", password="raketa123")
        response = self.user_client.logout_user(user=user, token='')
        assert response.status_code == 401
        assert response.json().get('token') is None






