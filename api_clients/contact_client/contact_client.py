import requests
from pydantic import BaseModel

from api_clients.contact_client.models.requests.contact_model import ContactModel
from api_clients.contact_client.models.requests.create_contact_model import CreateContact
from api_clients.contact_client.models.response.create_contact_response_model import CreateContactResponse

base_url = 'https://thinking-tester-contact-list.herokuapp.com/contacts/' ## + id GET/PUT/PATCH/DELETE

default_headers = {'Content-Type':'application/json'}
headers = dict()

def add_contact(contact: CreateContact, token: str):
    headers['Authorization'] = f'Bearer {token}'
    return requests.post(base_url, data=contact.model_dump_json(), headers=headers | default_headers)

def get_contact_list(token: str):
    headers['Authorization'] = f'Bearer {token}'
    return requests.get(base_url, headers=headers | default_headers)

def get_contact(contact_id:str, token:str):
    headers['Authorization'] = f'Bearer {token}'
    return requests.get(base_url + contact_id, headers=headers)

def put_contact(contact_id:str, token:str, data: CreateContact):
    headers['Authorization'] = f'Bearer {token}'
    return requests.put(base_url + contact_id, headers=headers | default_headers, data=data.model_dump_json())

def update_contact(contact_id:str, token:str, data: str):
    headers['Authorization'] = f'Bearer {token}'
    return requests.patch(base_url + contact_id, data=data, headers=headers | default_headers)

def delete_contact(contact_id:str, token:str):
    headers['Authorization'] = f'Bearer {token}'
    return requests.delete(base_url + contact_id, headers=headers)