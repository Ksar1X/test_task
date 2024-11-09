from pydantic import BaseModel


class AddedUser(BaseModel):
    _id:str
    firstName:str
    lastName:str
    email:str
