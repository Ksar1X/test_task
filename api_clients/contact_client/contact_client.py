import requests
from api_clients.api_clients_base import ApiClientBase
from api_clients.contact_client.models.requests.create_contact_model import CreateContact


headers = dict()

class ContactClient(ApiClientBase):

    contact_url = '/contacts'

    def add_contact(self, contact: CreateContact, token: str):
        headers['Authorization'] = f'Bearer {token}'
        return ApiClientBase.post_req(data=contact.model_dump_json(), postfix_url=self.contact_url)

    def get_contact_list(self, token: str):
        headers['Authorization'] = f'Bearer {token}'
        return ApiClientBase.post_req(postfix_url=self.contact_url, token=headers)

    def get_contact(self, contact_id:str, token:str):
        headers['Authorization'] = f'Bearer {token}'
        return ApiClientBase.post_req(postfix_url=self.contact_url + '/' + contact_id, token=headers)

    def put_contact(self, contact_id:str, token:str, data: CreateContact):
        headers['Authorization'] = f'Bearer {token}'
        return ApiClientBase.post_req(data=data.model_dump_json(), postfix_url=self.contact_url + '/' + contact_id, token=headers)

    def update_contact(self, contact_id:str, token:str, data: str):
        headers['Authorization'] = f'Bearer {token}'
        return ApiClientBase.post_req(data=data.model_dump_json(), postfix_url=self.contact_url + '/' + contact_id, token=headers)

    def delete_contact(self, contact_id:str, token:str):
        headers['Authorization'] = f'Bearer {token}'
        return ApiClientBase.post_req(postfix_url=self.contact_url + '/' + contact_id, token=headers)