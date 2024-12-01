from faker import Faker
from api_clients.contact_client.models.requests.create_contact_model import CreateContact


class ContactGenerator(Faker):

    def generate(self):
        contact = CreateContact(firstName=self.first_name(),
                                lastName=self.last_name(),
                                birthdate=self.date(), email=self.email(), phone='12345678',
                                street1=self.city(), street2=self.city(), city=self.city(),
                                stateProvince=self.current_country_code(), postalCode=self.postalcode(),
                                country=self.country())
        return contact

