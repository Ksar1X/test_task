from api_clients.user_client import user_client
from api_clients.user_client.models.requests.user import User


url = 'https://thinking-tester-contact-list.herokuapp.com/users/login'


def test_registered_user_able_login():
    payload = User(email="garynych@gmail.com", password="raketa123")
    response = user_client.login_user(payload).json()
    assert response.status_code == 200
    assert response.json().get('token') is not None

def test_unregistered_user_able_login():
    payload = User(email="qwerrsfgsv@gmail.com", password="raketa1234")
    response = user_client.login_user(payload)
    assert response.status_code == 401

def test_registered_user_with_incorrect_pas_cannot_login():
    payload = User(email="garynychxxx@gmail.com", password="q")
    response = user_client.login_user(payload)
    assert response.status_code == 401

def test_cannot_logout_without_login():
    payload = User(email="garynychxxx@gmail.com", password="raketa1234")
    response = user_client.logout_user(payload, None)
    assert response.status_code == 401

def test_logout_user():
    payload = User(email="joedoe1321@gmail.com", password="Qwerty1234")
    response = user_client.login_user(payload)
    response = user_client.logout_user(payload, response.json().get('token'))
    assert response.status_code == 200







