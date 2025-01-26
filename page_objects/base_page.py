from tests.singleton import WebDriverSingleton

class BasePage:

    def __init__(self):
        self.driver = WebDriverSingleton().get_driver()

    base_url = "https://thinking-tester-contact-list.herokuapp.com"
    sing_up_url = "https://thinking-tester-contact-list.herokuapp.com/addUser"
    contact_url = "https://thinking-tester-contact-list.herokuapp.com/contactList"
    add_contact_url = "https://thinking-tester-contact-list.herokuapp.com/addContact"
    contact_details_url = "https://thinking-tester-contact-list.herokuapp.com/contactDetails"

    @staticmethod
    def close_browser():
        WebDriverSingleton.quit_driver()
