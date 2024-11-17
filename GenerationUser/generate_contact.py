from faker import *

from api_clients.contact_client.models.requests.create_contact_model import CreateContact


class ContactGenerator:

    @staticmethod
    def generate(self):
        faker = Faker()
        contact = CreateContact(firstName=faker.first_name(),
                                lastName=faker.last_name(),
                                birthdate=faker.date(), email=faker.email(), phone=faker.phone_number(),
                                street1=faker.address(), street2=faker.address_detail(), city=faker.city(),
                                stateProvince=faker.state_name(), postalCode=faker.postalcode(),
                                country=faker.country())
        return contact
