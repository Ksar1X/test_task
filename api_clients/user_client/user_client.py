import requests

from api_clients.api_clients_base import ApiClientBase
from api_clients.user_client.models.requests.create_user_model import CreateUser
from api_clients.user_client.models.requests.user import User

headers = dict()

class UserClient(ApiClientBase):

    login_url = '/users/login'       ## login POST
    profile_url = '/users/me'        ## getUser, deleteUser, updateUser GET/ DELETE/ PATCH
    users_url = '/users'             ## addUser      POST
    logout_url = '/users/logout'     ## logout POST

    default_headers = {'Content-Type':'application/json'}


    def add_user(self, user: CreateUser):
        return ApiClientBase.post_req(postfix_url=self.users_url, data=user)

    def get_user_profile(self, token: str):
        headers['Authorization'] = f'Bearer {token}'
        return ApiClientBase.get_req(postfix_url=self.profile_url, token=headers)

    def login_user(self, user: User):
        return ApiClientBase.post_req(data=user, postfix_url=self.login_url)

    def logout_user(self, user: User, token: str):
        headers['Authorization'] = f'Bearer {token}'
        return ApiClientBase.post_req(data=user, postfix_url=self.logout_url, token=headers)

    def update_user(self, user: User, token: str):
        headers['Authorization'] = f'Bearer {token}'
        return ApiClientBase.patch_req(data=user, postfix_url=self.profile_url, token=headers)

    def delete_user(self, user:User, token: str):
        headers['Authorization'] = f'Bearer {token}'
        return ApiClientBase.post_req(data=user, postfix_url=self.profile_url, token=headers)

