from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from tests.singleton import Singleton


class BasePage:

    base_url = "https://thinking-tester-contact-list.herokuapp.com"
    sing_up_url = "https://thinking-tester-contact-list.herokuapp.com/addUser"
    contact_url = "https://thinking-tester-contact-list.herokuapp.com/contactList"
    add_contact_url = "https://thinking-tester-contact-list.herokuapp.com/addContact"
    contact_details_url = "https://thinking-tester-contact-list.herokuapp.com/contactDetails"

    driver = Singleton()
    wait = WebDriverWait(driver, 15, poll_frequency=1)

    actions = ActionChains(driver)
