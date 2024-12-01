from pydantic import BaseModel


class ContactField(BaseModel):
    firstName: str
