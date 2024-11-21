from faker import Faker
from api_clients.contact_client.models.requests.create_contact_model import CreateContact


class ContactGenerator(Faker):

    def generate(self):
        contact = CreateContact(firstName=self.first_name(),
                                lastName=self.last_name(),
                                birthdate=self.date(), email=self.email(), phone=self.phone_number(),
                                street1=self.address(), street2=self.address_detail(), city=self.city(),
                                stateProvince=self.state_name(), postalCode=self.postalcode(),
                                country=self.country())
        return contact
