from pydantic import BaseModel

from api_clients.user_client.models.requests.create_user_model import CreateUser


class CreateUserResponse(BaseModel):
    user: CreateUser
    token: str