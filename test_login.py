import requests

from api_clients.user_client import user_client
from api_clients.user_client.models.requests.user import User

url = 'https://thinking-tester-contact-list.herokuapp.com/users/login'

def test_registered_user_able_login():
    payload = User(email="garynych@gmail.com", password="raketa123")
    response = user_client.login_user(payload)
    assert response.status_code == 200
    assert response.json().get('token') is not None

def test_unregistered_user_able_login():
    payload = User(email="qwerrsfgsv@gmail.com", password="raketa1234").model_dump_json()
    response = requests.post(url=url, data=payload, headers={'Content-Type': 'application/json'})
    assert response.status_code == 401

def test_registered_user_with_incorrect_pas_cannot_login():
    payload = User(email="garynychxxx@gmail.com", password="raketa1234").model_dump_json()
    response = requests.post(url= url, data=payload, headers={'Content-Type': 'application/json'})
    assert response.status_code == 401




