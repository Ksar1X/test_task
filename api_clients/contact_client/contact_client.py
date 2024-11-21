import requests
from api_clients.api_clients_base import ApiClientBase
from api_clients.contact_client.models.requests.create_contact_model import CreateContact
from pydantic import BaseModel


class ContactClient(ApiClientBase):

    contact_url = '/contacts'
    api = ApiClientBase()

    def add_contact(self, contact: CreateContact, token: str):
        return self.api.post_req(data=contact, postfix_url=self.contact_url, token=token)

    def get_contact_list(self, token: str):
        return self.api.get_req(postfix_url=self.contact_url, token=token)

    def get_contact(self, contact_id:str, token: str):
        return self.api.get_req(postfix_url=self.contact_url + '/' + contact_id, token=token)

    def put_contact(self, contact_id:str, token: str, data: CreateContact):
        return self.api.put_req(data=data, postfix_url=self.contact_url + '/' + contact_id, token=token)

    def update_contact(self, contact_id:str, token: str, data: str):
        return self.api.patch_req(data=data, postfix_url=self.contact_url + '/' + contact_id, token=token)

    def delete_contact(self, contact_id:str, token: str):
        return self.api.delete_req(postfix_url=self.contact_url + '/' + contact_id, token=token)