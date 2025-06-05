from beanie import init_beanie
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from models import ClientModel, UpdateClientModel
from config import settings

async def init_db():
    client = AsyncIOMotorClient(settings.MONGO_URI)
    try:
        await init_beanie(database=client[settings.MONGO_DB_NAME], document_models=[ClientModel])
        return True
    except Exception as e:
        return e


async def add_client(client_data: ClientModel):
    client_to_add = ClientModel(**client_data.model_dump())
    try:
        result = await client_to_add.insert()
    except Exception as e:
        result = e
    return result


async def get_clients():
    founded_clients = await ClientModel.find_all().to_list()
    return founded_clients
     

async def update_client(desired_cpf: str, data_to_update: UpdateClientModel):
    desired_client = await ClientModel.find_one(ClientModel.cpf == desired_cpf)
    if desired_client:
        for campo, valor in data_to_update.model_dump(exclude_unset=True).items():
            setattr(desired_client, campo, valor)

        result = await desired_client.save()
        if result:
            return {"message": f"Cliente com CPF {desired_cpf} alterado com sucesso."}
        else:
            raise HTTPException(status_code=404, detail=f"Cliente com CPF {desired_cpf} não encontrado.") 
    else:
        raise HTTPException(status_code=404, detail=f"Cliente com CPF {desired_cpf} não encontrado.")



async def delete_client(desired_cpf: str):
    desired_client = await ClientModel.find_one(ClientModel.cpf == desired_cpf)
    if desired_client:
        result = await desired_client.delete()
        if result.deleted_count == 1:
            return {"message": f"Cliente com CPF {desired_cpf} deletado com sucesso."}
        else:
            raise HTTPException(status_code=404, detail=f"Cliente com CPF {desired_cpf} não encontrado.")
    else:
        raise HTTPException(status_code=404, detail=f"Cliente com CPF {desired_cpf} não encontrado.")
        
         
