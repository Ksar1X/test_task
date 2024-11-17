import requests

from api_clients.api_clients_base import ApiClientBase
from api_clients.user_client.models.requests.create_user_model import CreateUser
from api_clients.user_client.models.requests.user import User


class UserClient(ApiClientBase):

    base_url = 'https://thinking-tester-contact-list.herokuapp.com'



    login_url = base_url + '/users/login'       ## login POST
    profile_url = base_url + '/users/me'        ## getUser, deleteUser, updateUser GET/ DELETE/ PATCH
    users_url = '/users'             ## addUser      POST
    logout_url = base_url + '/users/logout'     ## logout POST

    default_headers = {'Content-Type':'application/json'}

    def add_user(self, user: CreateUser):
        return  ApiClientBase.post_req(postfix_url=self.users_url, data=user)

    def get_user_profile(user_id: str, token: str):
        headers = dict()
        headers['Authorization'] = f'Bearer {token}'
        return requests.get(url=profile_url + f"/{user_id}", headers=headers | default_headers)

    def login_user(user: User):
        return requests.post(url=login_url, data=user.model_dump_json(), headers=default_headers)

    def logout_user(user: User, token: str):
        headers = dict()
        headers['Authorization'] = f'Bearer {token}'
        return requests.post(url=logout_url, data=user.model_dump_json(), headers=headers | default_headers)

    def update_user(user: User, token: str):
        headers = dict()
        headers['Authorization'] = f'Bearer {token}'
        return requests.patch(url=profile_url, data=user.model_dump_json(), headers=headers | default_headers)

    def delete_user(user:User, token: str):
        headers=dict()
        headers['Authorization'] = f'Bearer {token}'
        return requests.delete(url=profile_url, data=user.model_dump_json(), headers=headers | default_headers)

