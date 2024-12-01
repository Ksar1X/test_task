from faker import Faker

from api_clients.user_client.models.requests.create_user_model import CreateUser


class GenerateUser(Faker):

    def generate(self):
        user = CreateUser(firstName=self.first_name(), lastName=self.last_name(), email=self.word() + self.email(), password=self.password())
        return user