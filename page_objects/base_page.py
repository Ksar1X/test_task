from tests.singleton import WebDriverSingleton


class BasePage:

    def __init__(self):
        self.driver = WebDriverSingleton().get_driver()


    base_url = "https://thinking-tester-contact-list.herokuapp.com"
    sing_up_url = "https://thinking-tester-contact-list.herokuapp.com/addUser"
    contact_url = "https://thinking-tester-contact-list.herokuapp.com/contactList"
    add_contact_url = "https://thinking-tester-contact-list.herokuapp.com/addContact"
    contact_details_url = "https://thinking-tester-contact-list.herokuapp.com/contactDetails"


    def close_browser(self):
        WebDriverSingleton.quit_driver()

