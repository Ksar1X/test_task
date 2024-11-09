from faker import Faker

from api_clients.user_client.models.requests.create_user_model import CreateUser


class UserGenerator:

    @staticmethod
    def generate():
        faker = Faker()
        return CreateUser(firstName=faker.first_name(), lastName=faker.last_name(), email=faker.email(), password=faker.password())