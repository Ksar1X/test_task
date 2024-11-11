from pydantic import BaseModel, Field

from api_clients.contact_client.models.requests.create_contact_model import CreateContact


class CreateContactResponse(CreateContact):
    id:str = Field(alias='_id')
    owner: str
