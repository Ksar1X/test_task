import requests
from api_clients.api_clients_base import ApiClientBase
from api_clients.contact_client.models.requests.create_contact_model import CreateContact


headers = dict()

class ContactClient(ApiClientBase):

    contact_url = '/contacts'
    api = ApiClientBase()

    def add_contact(self, contact: CreateContact, token: dict):
        headers['Authorization'] = f'Bearer {token}'
        return self.api.post_req(data=contact, postfix_url=self.contact_url)

    def get_contact_list(self, token: dict):
        headers['Authorization'] = f'Bearer {token}'
        return self.api.get_req(postfix_url=self.contact_url, token=headers)

    def get_contact(self, contact_id:str, token: dict):
        headers['Authorization'] = f'Bearer {token}'
        return self.api.get_req(postfix_url=self.contact_url + '/' + contact_id, token=headers)

    def put_contact(self, contact_id:str, token: dict, data: CreateContact):
        headers['Authorization'] = f'Bearer {token}'
        return self.api.put_req(data=data, postfix_url=self.contact_url + '/' + contact_id, token=headers)

    def update_contact(self, contact_id:str, token: dict, data: str):
        headers['Authorization'] = f'Bearer {token}'
        return self.api.patch_req(data=data, postfix_url=self.contact_url + '/' + contact_id, token=headers)

    def delete_contact(self, contact_id:str, token: dict):
        headers['Authorization'] = f'Bearer {token}'
        return self.api.delete_req(postfix_url=self.contact_url + '/' + contact_id, token=headers)