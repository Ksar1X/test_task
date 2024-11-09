import requests

from api_clients.user_client.models.requests.create_user_model import CreateUser
from api_clients.user_client.models.requests.user import User
from api_clients.user_client.models.response.added_user import AddedUser
from api_clients.user_client.models.response.create_user_response_model import CreateUserResponse

base_url = 'https://thinking-tester-contact-list.herokuapp.com'

login_url = base_url + '/users/login'       ## login POST
profile_url = base_url + '/users/me'        ## getUser, deleteUser, updateUser GET/ DELETE/ PATCH
users_url = base_url + '/users'             ## addUser      POST
logout_url = base_url + '/users/logout'     ## logout POST


default_headers = {'Content-Type':'application/json'}

def add_user(user: CreateUser):
    response = requests.post(url=users_url, data=user.model_dump_json(), headers=default_headers)
    return CreateUserResponse(**response.json())

def get_user_profile(user_id: str, token: str):
    headers = default_headers
    headers.pop('Authorization', f'Bearer {token}')
    response = requests.get(url=profile_url + f"/{user_id}", headers=headers)
    return CreateUserResponse(**response.json())

def login_user(user: User):
    response = requests.post(url=login_url, data=user.model_dump_json(), headers=default_headers)
    return CreateUserResponse(user=response.json().get('user'), token=response.json().get('token'))

def logout_user(user: User, token: str):
    headers = default_headers
    headers.pop('Authorization', f'Bearer {token}')
    response = requests.post(url=logout_url, data=user.model_dump_json(), headers=headers)
    return CreateUserResponse(**response.json())

def update_user(user_id: str, token: str):
    headers = default_headers
    headers.pop('Authorization', f'Bearer {token}')
    response = requests.patch(url=profile_url + f"/{user_id}", headers=headers)
    return CreateUserResponse(**response.json())

def delete_user(user_id: str, token: str):
    headers = default_headers
    headers.pop('Authorization', f'Bearer {token}')
    response = requests.delete(url=profile_url + f"/{user_id}", headers=headers)
    return CreateUserResponse(**response.json())