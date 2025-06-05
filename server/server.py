import db_handle
from models import UpdateClientModel
from config import DEBUG_MODE
from fastapi import FastAPI
from routes import router


app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def on_startup():
    await db_handle.init_db()
