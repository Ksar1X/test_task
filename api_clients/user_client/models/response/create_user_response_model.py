from pydantic import BaseModel

from api_clients.user_client.models.response.added_user import AddedUser


class CreateUserResponse(BaseModel):
    user: AddedUser
    token: str