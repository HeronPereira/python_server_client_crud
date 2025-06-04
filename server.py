import db_handle
from models import UpdateClientModel
from config import DEBUG_MODE
from fastapi import FastAPI
from routes import router


async def direct_crud_test():
    started_db = await db_handle.init_db()
    if started_db:
        print("---------------------Adding clients---------------------")
        added_client = await db_handle.add_client(nome_in="foo", email_in="foo@foo.com",cpf_in="00000000000")
        print("return of added client zezinho: ", added_client)
        added_client = await db_handle.add_client(nome_in="bar", email_in="bar@bar.com",cpf_in="00000000001")
        print("return of added client bar: ", added_client)
        added_client = await db_handle.add_client(nome_in="baz", email_in="baz@exemplo.com",cpf_in="00000000002")
        print("return of added client baz: ", added_client)
        print("---------------------Showing clients---------------------")
        clients_list = await db_handle.get_clients()
        print("Clients at the db: ", clients_list)
        print("---------------------Update baz client email---------------------")
        print("from: baz@exemplo.com")
        print("to: baz@baz.com")
        print("founded based on: CPF: 00000000002")
        updated_client = await db_handle.update_client(desired_cpf="00000000002", data_to_update=UpdateClientModel(email="baz@baz.com"))
        print("Result of the update: ", updated_client)
        print("---Show the updated list---")
        print(await db_handle.get_clients())
        print("---------------------Delete baz client---------------------")
        print("founded based on: CPF: 00000000002")
        deleted_client = await db_handle.delete_client(desired_cpf="00000000002")
        print("Result of deleted client: ", deleted_client)
        print("---Show the updated list---")
        print(await db_handle.get_clients())

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def on_startup():
    await db_handle.init_db()
#async def main():
#    if DEBUG_MODE:
        #direct_crud_test()

        

#if __name__ == '__main__':
#    asyncio.run(main())