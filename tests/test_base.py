from api_clients.contact_client.contact_client import ContactClient
from api_clients.user_client.user_client import UserClient
from generators.generate_contact import ContactGenerator
from generators.generate_unregistered_user import GenerateUser


class BaseTest:
    user_client = UserClient()
    contact_client = ContactClient()
    random_user = GenerateUser()
    random_contact = ContactGenerator()
