from _pytest.fixtures import fixture
from api_clients.user_client.models.requests.user import User
from tests.test_base import BaseTest


class TestLogIn(BaseTest):

    @fixture(scope='class')
    def create_user_fixture(self):
        user = self.random_user.generate()
        self.user_client.add_user(user=user)
        yield user
        user = User(email=user.email, password=user.password)
        response = self.user_client.login_user(user=user)
        response = self.user_client.delete_user(token=response.json().get('token'))
        assert response.status_code == 200


    @fixture(scope='class')
    def get_user_token_fixture(self, create_user_fixture):
        user = create_user_fixture
        response = self.user_client.login_user(user=User(email=user.email, password=user.password))
        token = response.json().get('token')
        yield user, token

    def test_registered_user_able_login(self, create_user_fixture):
        user = create_user_fixture
        response = self.user_client.login_user(user=user)
        assert response.status_code == 200
        assert response.json().get('token') is not None

    def test_unregistered_user_able_login(self):
        user = self.random_user.generate()
        response = self.user_client.login_user(user=User(email=user.email, password=user.password))
        assert response.status_code == 401


    def test_registered_user_with_incorrect_pas_cannot_login(self, create_user_fixture):
        user = create_user_fixture
        response = self.user_client.login_user(user=User(email=user.email, password='qwerty'))
        assert response.status_code == 401


    def test_logout_user(self, get_user_token_fixture):
        user, user_token = get_user_token_fixture
        response = self.user_client.logout_user(user=user, token=user_token)
        assert response.status_code == 200

    def test_user_cannot_logout_without_login(self, create_user_fixture):
        user = create_user_fixture
        response = self.user_client.logout_user(user=user, token='')
        assert response.status_code == 401
        assert response.json().get('token') is None






