from pydantic import BaseModel

class CreateContact(BaseModel):
    firstName: str
    lastName: str
    birthdate: str
    email: str
    phone: str
    street1: str
    street2: str
    city: str
    stateProvince: str
    postalCode: str
    country: str
    owner: str
