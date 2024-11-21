import requests

from api_clients.api_clients_base import ApiClientBase
from api_clients.user_client.models.requests.create_user_model import CreateUser
from api_clients.user_client.models.requests.user import User


class UserClient(ApiClientBase):

    login_url = '/users/login'       ## login POST
    profile_url = '/users/me'        ## getUser, deleteUser, updateUser GET/ DELETE/ PATCH
    users_url = '/users'             ## addUser      POST
    logout_url = '/users/logout'     ## logout POST

    api = ApiClientBase()

    def add_user(self, user: CreateUser):
        return self.api.post_req(postfix_url=self.users_url, data=user)

    def get_user_profile(self, token: str):
        return self.api.get_req(postfix_url=self.profile_url, token=token)

    def login_user(self, user: User):
        return self.api.post_req(data=user, postfix_url=self.login_url)

    def logout_user(self, user: User, token: str):
        return self.api.post_req(data=user, postfix_url=self.logout_url, token=token)

    def update_user(self, user: User, token: str):
        return self.api.patch_req(data=user, postfix_url=self.profile_url, token=token)

    def delete_user(self, token: str):
        return self.api.delete_req(postfix_url=self.profile_url, token=token)

