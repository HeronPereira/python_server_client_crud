import db_handle
from models import ClientModel, UpdateClientModel
from fastapi import APIRouter

router = APIRouter()

@router.get("/get")
async def get_clients():
    return await db_handle.get_clients()

@router.post("/add")
async def set_client(client_data: ClientModel):
    return await db_handle.add_client(client_data=client_data)

@router.put("/update/{cpf}")
async def update_client(cpf: str, update_data:UpdateClientModel):
    await db_handle.update_client(desired_cpf=cpf, data_to_update=update_data)

@router.delete("/delete/{cpf}")
async def delete_client(cpf: str):
    return await db_handle.delete_client(cpf)