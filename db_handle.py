from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models import ClientModel, UpdateClientModel
from config import MONGO_DB_NAME, MONGO_URI

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    try:
        await init_beanie(database=client[MONGO_DB_NAME], document_models=[ClientModel])
        return True
    except Exception as e:
        return e


async def add_client(nome_in,email_in,cpf_in):
    client_to_add = ClientModel(nome=nome_in, email=email_in, cpf=cpf_in)
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
        try:
            result = await desired_client.save()
        except Exception as e:
            result = e
        return result
    else:
        return desired_client
        

async def delete_client(desired_cpf: str):
    desired_client = await ClientModel.find_one(ClientModel.cpf == desired_cpf)
    if desired_cpf:
        try:
            result = await desired_client.delete()
        except Exception as e:
            result = e
        return result
    else:
        return desired_client

   
