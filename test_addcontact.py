import requests
from models.create_contact_model import CreateContact
from pytest import fixture

class TestAddContact:
    url = "https://thinking-tester-contact-list.herokuapp.com/contacts"
    def test_add_contact(self):
        payload = CreateContact(firstName="Joe",lastName="Doe",birthdate="1999-10-10",email="jordann723@gmail.com",phone="503645570",street1="Варшавская",street2="Boharterów Monte Cassino",city="Białystok",stateProvince="KS",postalCode="15-873",country="Польша", owner="").model_dump_json()
        response = requests.post(url=self.url, data=payload, headers={'Content-Type': 'application/json'})
        assert response.status_code == 200
