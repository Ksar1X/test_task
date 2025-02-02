from api_clients.user_client.models.requests.user import User
from tests.test_base import BaseTest


class TestLogIn(BaseTest):

    def test_registered_user_able_login(self, create_and_delete_user_fixture):
        user = create_and_delete_user_fixture
        response = self.user_client.login_user(user=user)
        assert response.status_code == 200
        assert response.json().get('token') is not None

    def test_unregistered_user_able_login(self):
        user = self.random_user.generate()
        response = self.user_client.login_user(user=User(email=user.email, password=user.password))
        assert response.status_code == 401

    def test_registered_user_with_incorrect_pas_cannot_login(self, create_and_delete_user_fixture):
        user = create_and_delete_user_fixture
        response = self.user_client.login_user(user=User(email=user.email, password='qwerty'))
        assert response.status_code == 401

    def test_logout_user(self, user_get_token_fixture):
        user_token, user = user_get_token_fixture
        response = self.user_client.logout_user(user=user, token=user_token)
        assert response.status_code == 200

    def test_user_cannot_logout_without_login(self, create_and_delete_user_fixture):
        user = create_and_delete_user_fixture
        response = self.user_client.logout_user(user=user, token='')
        assert response.status_code == 401
        assert response.json().get('token') is None






