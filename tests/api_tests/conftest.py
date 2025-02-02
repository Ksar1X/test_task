import pytest
from api_clients.user_client.models.requests.user import User
from tests.test_base import BaseTest

base_test = BaseTest()

@pytest.fixture()
def create_and_delete_user_fixture():
    user = base_test.random_user.generate()
    base_test.user_client.add_user(user=user)
    yield user
    user = User(email=user.email, password=user.password)
    response = base_test.user_client.login_user(user=user)
    response = base_test.user_client.delete_user(token=response.json().get('token'))
    assert response.status_code == 200

@pytest.fixture()
def user_get_token_fixture(create_and_delete_user_fixture):
    user = create_and_delete_user_fixture
    response = base_test.user_client.login_user(user=User(email=user.email, password=user.password))
    yield response.json().get('token'), user

@pytest.fixture()
def get_contact_id_fixture(user_get_token_fixture):
    token, user = user_get_token_fixture
    base_test.user_client.login_user(user=User(email=user.email, password=user.password))
    contact = base_test.random_contact.generate()
    response = base_test.contact_client.add_contact(data=contact, token=token)
    identification = response.json().get('_id')
    yield identification

