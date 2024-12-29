from selenium.webdriver.support.wait import WebDriverWait

from page_objects.pages.contact_list_page import ContactListPage
from page_objects.pages.contact_page import ContactPage
from page_objects.pages.login_page import LoginPage
from page_objects.pages.singup_page import SingUpPage
from tests.singleton import Singleton
from tests.test_base import BaseTest


class BaseUiTest(BaseTest):

    base_url = "https://thinking-tester-contact-list.herokuapp.com"
    sing_up_url = "https://thinking-tester-contact-list.herokuapp.com/addUser"
    contact_url = "https://thinking-tester-contact-list.herokuapp.com/contactList"
    add_contact_url = "https://thinking-tester-contact-list.herokuapp.com/addContact"

    login_page = LoginPage()
    singUp_page = SingUpPage()
    contact_list_page = ContactListPage()
    contact_page = ContactPage()

    driver = Singleton()
    wait = WebDriverWait(driver, 15, poll_frequency=1)