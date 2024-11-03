from pydantic import BaseModel

from models.create_user_model import CreateUser


class CreateUserResponse(BaseModel):
    user: CreateUser
    token: str