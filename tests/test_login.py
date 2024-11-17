from api_clients.api_clients_base import token_header
from api_clients.user_client.user_client import *

url = 'https://thinking-tester-contact-list.herokuapp.com/users/login'



class TestLogIn:

    def test_registered_user_able_login(self):
        payload = User(email="garynych@gmail.com", password="raketa123")
        response = login_user()
        print(response)
        assert response.status_code == 200
        assert response.json().get('token') is not None

    def test_unregistered_user_able_login(self):
        payload = User(email="qwerrsfgsv@gmail.com", password="raketa1234")
        response = ApiClientBase.post_req(data=payload, postfix_url='/users/login')
        assert response.status_code == 401

    def test_registered_user_with_incorrect_pas_cannot_login(self):
        payload = User(email="garynychxxx@gmail.com", password="q")
        response = ApiClientBase.post_req(data=payload, postfix_url='/users/login')
        assert response.status_code == 401

    def test_cannot_logout_without_login(self):
        payload = User(email="garynychxxx@gmail.com", password="raketa1234")
        response = ApiClientBase.post_req(data=payload, postfix_url='/users/login')
        assert response.status_code == 401

    def test_logout_user(self):
        profile = User(email="garynychxxx@gmail.com", password="raketa123")
        res = ApiClientBase.post_req(data=profile, postfix_url='/users/login')
        token_header['Authorization'] = res.json().get('token')
        response = ApiClientBase.post_req(data=profile, postfix_url='/users/logout')
        assert response.status_code == 200

    def test_user_cannot_logout_without_login(self):
        profile = User(email="garynychxxx@gmail.com", password="raketa123")
        response = ApiClientBase.post_req(data=profile, postfix_url='/users/logout')
        assert response.status_code == 401
        assert response.json().get('token') is None






