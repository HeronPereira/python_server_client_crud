from beanie import Document
from pydantic import BaseModel,EmailStr, Field
from typing import Optional

class ClientModel(Document):
    nome: str = Field(..., min_length=1)
    email: EmailStr
    cpf: str = Field(...,min_length=11, max_length=11)

    class Settings:
        name="clientes"


class UpdateClientModel(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    cpf: Optional[str] = None