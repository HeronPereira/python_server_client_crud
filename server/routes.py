import db_handle
import hash_password
from models import ClientModel, UpdateClientModel, LoginModel
from fastapi import APIRouter, HTTPException, Depends
from mock_login import FAKE_USER
from auth import create_token, verify_token


router = APIRouter()

@router.get("/get")
async def get_clients(user: str = Depends(verify_token)):
    return await db_handle.get_clients()

@router.post("/add")
async def set_client(client_data: ClientModel, user: str = Depends(verify_token)):
    return await db_handle.add_client(client_data=client_data)

@router.put("/update/{cpf}")
async def update_client(cpf: str, update_data:UpdateClientModel, user: str = Depends(verify_token)):
    await db_handle.update_client(desired_cpf=cpf, data_to_update=update_data)

@router.delete("/delete/{cpf}")
async def delete_client(cpf: str, user: str = Depends(verify_token)):
    return await db_handle.delete_client(cpf)

@router.post("/login")
async def login(dados: LoginModel):
    if dados.username != FAKE_USER["username"] or not hash_password.verify_encoded_password(dados.password, FAKE_USER["password"]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    
    token = create_token(dados.username)
    return  {"access_token": token, "token_type": "bearer"}

