from api_clients.contact_client.contact_client import ContactClient
from api_clients.user_client.models.requests.user import User
from page_objects.base_page import BasePage
from api_clients.user_client.user_client import UserClient

class ContactListPage(BasePage):

    ADD_CONTACT_BUTTON = ("xpath", "//button[@id='add-contact']")
    CONTACT_ROW = ("xpath", "//td[1]")

    user_client = UserClient()
    contact_client = ContactClient()


    def add_contact(self):
        self.driver.find_element(*self.ADD_CONTACT_BUTTON).click()

    def click_on_contact(self, email):
        self.driver.find_element(*("xpath","//td[text()="f'{email}'"]"))









    def get_contact_list(self):
        user = User(email='garynychxxx@gmail.com', password='raketa123')
        response = self.user_client.add_user(user)
        token = response.json().get('token')
        response = self.contact_client.get_contact_list(token=token)










