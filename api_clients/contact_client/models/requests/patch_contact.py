from pydantic import BaseModel


class PatchContactModel(BaseModel):
    firstName: str