import requests

from api_clients.contact_client.models.create_contact_model import CreateContact


base_url = 'https://thinking-tester-contact-list.herokuapp.com/contacts/' ## + id GET/PUT/PATCH/DELETE

default_headers = {'Content-Type':'application/json'}
headers = dict()

def add_contact(contact: CreateContact, token: str):
    headers['Authorization'] = f'Bearer {token}'
    return requests.post(base_url[:-1], data=contact.model_dump_json(), headers=headers)

def get_contact_list(token: str):
    headers['Authorization'] = f'Bearer {token}'
    return requests.post(base_url[:-1], headers=headers)

def get_contact(contact_id:str, token:str):
    headers['Authorization'] = f'Bearer {token}'
    return requests.get(base_url + contact_id, headers=headers)

def delete_contact(contact_id:str, token:str):
    headers['Authorization'] = f'Bearer {token}'
    return requests.delete(base_url + contact_id, headers=headers)