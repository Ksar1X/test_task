from page_objects.add_contact_page import AddContactPage
from page_objects.base_page import BasePage
from page_objects.contact_details_page import ContactDetailsPage
from page_objects.contact_list_page import ContactListPage
from page_objects.edit_contact_page import EditContactPage
from page_objects.login_page import LoginPage
from page_objects.singup_page import SingUpPage
from tests.test_base import BaseTest

class TestBaseUi(BaseTest):

    login_page = LoginPage()
    singUp_page = SingUpPage()
    contact_list_page = ContactListPage()
    add_contact_page = AddContactPage()
    base_page = BasePage()
    contact_details_page = ContactDetailsPage()
    edit_contact_page = EditContactPage()

