import asyncio
import httpx
from config import BASE_URL, CREDENTIALS


async def login_get_token(credentials):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{BASE_URL}/login", json=credentials)          
            response.raise_for_status()
            token = response.json().get("access_token")
            if not token:
                raise ValueError("Token não encontrado!")
            else:
                return token
        except httpx.HTTPStatusError as e:
            print(f"Erro HTTP ao fazer login: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")


async def get_clients(token: str):
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BASE_URL}/get", headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            print(f"Erro HTTP ao acessar o endpoint protegido: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")


async def add_client(token: str, client_data: dict):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/add", json=client_data, headers=headers)
        response.raise_for_status()
        response.json()


async def update_client(token: str, cpf: str, update_data: dict):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}/update/{cpf}", json=update_data, headers=headers)
        response.raise_for_status()
        return response.status_code


async def delete_client(token: str, cpf: str):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/delete/{cpf}", headers=headers)
        response.raise_for_status()
        return response.status_code
    
 
async def main():
    jwt_token = await login_get_token(CREDENTIALS)
    if jwt_token:
        print("Add client: ", {"nome": "foo","email": "foo@foo.com","cpf": "00000000000"})
        await add_client(jwt_token, {"nome": "foo","email": "foo@foo.com","cpf": "00000000000"})
        print("Add client: ", {"nome": "bar","email": "bar@bar.com","cpf": "00000000001"})
        await add_client(jwt_token, {"nome": "bar","email": "bar@bar.com","cpf": "00000000001"})
        print("Add client: ", {"nome": "baz","email": "baz@example.com","cpf": "00000000002"})
        await add_client(jwt_token, {"nome": "baz","email": "baz@example.com","cpf": "00000000002"})
        print("---Clientes do servidor---")
        clients_from_server = await get_clients(jwt_token)
        for c in clients_from_server:
            print(c)
        print("---Update client: ", {"nome": "baz","email": "baz@example.com","cpf": "00000000002"},"---")
        print("Change baz email from baz@example.com to baz@baz.com")
        update_response = await update_client(jwt_token, "00000000002",{"email":"baz@baz.com"})
        print("---Clientes Atualizados---")
        clients_from_server = await get_clients(jwt_token)
        for c in clients_from_server:
            print(c)
        print("---Delete client---")
        print("Delete 00000000000 client")
        delete_return = await delete_client(jwt_token, "00000000000")
        print("Delete 00000000001 client")
        delete_return = await delete_client(jwt_token, "00000000001")
        print("Delete 00000000002 client")
        delete_return = await delete_client(jwt_token, "00000000002")
        print("---Clientes Atualizados---")
        clients_from_server = await get_clients(jwt_token)
        for c in clients_from_server:
            print(c)


if __name__ == "__main__":
    asyncio.run(main())