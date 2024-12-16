from api_clients.contact_client.contact_client import ContactClient
from api_clients.user_client.user_client import UserClient
from generators.generate_contact import ContactGenerator
from generators.generate_unregistered_user import GenerateUser
from page_objects.contact_list_page import ContactListPage
from page_objects.login_page import LoginPage
from page_objects.singup_page import SingUpPage


class BaseTest:
    user_client = UserClient()
    contact_client = ContactClient()
    random_user = GenerateUser()
    random_contact = ContactGenerator()
    login_page = LoginPage()
    singUp_page = SingUpPage()
    contact_list_page = ContactListPage()
