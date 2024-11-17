from pydantic import BaseModel

class CreateUser(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str


