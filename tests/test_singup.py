from pytest import fixture
from Generators.generate_unregistered_user import GenerateUser
from api_clients.user_client.user_client import *

user_token_header = dict()

class TestSignUp:

    user_client = UserClient()
    random_user = GenerateUser()

    @fixture(scope='class')
    def create_user_fixture(self):
        user = self.random_user.generate()
        self.user_client.add_user(user=user)
        yield user

    @fixture(scope="class")
    def delete_user_fixture(self, create_user_fixture):
        user = create_user_fixture
        yield user
        user = User(email=user.email, password=user.password)
        response = self.user_client.login_user(user=user)
        response = self.user_client.delete_user(token=response.json().get('token'))
        assert response.status_code == 200

    def test_create_user_with_valid_fields(self):
        user = self.random_user.generate()
        response = self.user_client.add_user(user=user)
        assert response.status_code == 201

    def test_cannot_create_with_empty_fields(self):
        user = CreateUser(firstName="", lastName="", email="", password="")
        response = self.user_client.add_user(user=user)
        assert response.status_code == 400

    def test_create_user_with_incorrect_email_field(self):
        user = self.random_user.generate()
        response = self.user_client.add_user(user=CreateUser(firstName=user.firstName, lastName=user.lastName, email="asdasd3412@", password=user.password))
        assert response.status_code == 400
        assert response.json().get('message') == 'User validation failed: email: Email is invalid'

    def test_create_user_with_incorrect_pas_field(self):
        user = self.random_user.generate()
        response = self.user_client.add_user(
            user=CreateUser(firstName=user.firstName, lastName=user.lastName, email=user.email,
                            password='q'))
        assert response.status_code == 400
        assert response.json().get('message') == 'User validation failed: password: Path `password` (`q`) is shorter than the minimum allowed length (7).'

    def test_cannot_create_registered_user(self):
        user = CreateUser(firstName="Joe1", lastName="Doe1", email="joedoe@gmail.com",password="joedoe1234")
        response = self.user_client.add_user(user=user)
        assert response.status_code == 400
        assert response.json().get('message') == 'Email address is already in use'


    def test_cannot_delete_user_without_login(self, delete_user_fixture):
        user = delete_user_fixture
        response = self.user_client.delete_user(token='')
        print(response)
        assert response.status_code == 401

    def test_delete_user(self, create_user_fixture):
        user = create_user_fixture
        self.user_client.add_user(user=user)
        response = self.user_client.login_user(user=User(email=user.email, password=user.password))
        res = self.user_client.delete_user(token=response.json().get('token'))
        assert res.status_code == 200


    def test_update_user(self, delete_user_fixture):
        user = delete_user_fixture
        self.user_client.add_user(user=user)
        response = self.user_client.login_user(user=User(email=user.email, password=user.password))
        response = self.user_client.update_user(user=User(email=user.email, password=user.password), token=response.json().get('token'))
        assert response.status_code == 200

    def test_get_user_profile(self, delete_user_fixture):
        user = delete_user_fixture
        self.user_client.add_user(user=user)
        response = self.user_client.login_user(user=User(email=user.email, password=user.password))
        response = self.user_client.get_user_profile(token=response.json().get('token'))
        assert response.status_code == 200

