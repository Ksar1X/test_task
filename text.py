import requests


url = 'https://thinking-tester-contact-list.herokuapp.com/users/login'

def unregistered_user():
    payload = "{\n    \"email\": \"test2@fake.com\",\n    \"password\": \"myNewPassword\"\n}"
    response = requests.request("POST", url, data=payload)
    assert response.status_code == 401

