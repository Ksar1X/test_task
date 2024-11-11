import requests

from api_clients.user_client import user_client
from api_clients.user_client.user_client import *

url = 'https://thinking-tester-contact-list.herokuapp.com/users/login'

class TestLogIn:

    def test_registered_user_able_login(self):
        payload = User(email="garynych@gmail.com", password="raketa123")
        response = login_user(payload)
        assert response.status_code == 200
        assert response.json().get('token') is not None

    def test_unregistered_user_able_login(self):
        payload = User(email="qwerrsfgsv@gmail.com", password="raketa1234")
        response = login_user(payload)
        assert response.status_code == 401

    def test_registered_user_with_incorrect_pas_cannot_login(self):
        payload = User(email="garynychxxx@gmail.com", password="q")
        response = login_user(payload)
        assert response.status_code == 401

    def test_cannot_logout_without_login(self):
        payload = User(email="garynychxxx@gmail.com", password="raketa1234")
        response = user_client.logout_user(payload, '')
        assert response.status_code == 401

    def test_logout_user(self):
        profile = User(email="garynychxxx@gmail.com", password="raketa123")
        res = login_user(profile)
        response = logout_user(profile, res.json().get('token'))
        assert response.status_code == 200

    def test_user_cannot_logout_without_login(self):
        profile = User(email="garynychxxx@gmail.com", password="raketa123")
        response = logout_user(profile, '')
        assert response.status_code == 401






