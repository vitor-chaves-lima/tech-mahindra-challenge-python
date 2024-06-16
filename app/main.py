from fastapi import FastAPI

from core.db import engine, Base

from api.routes import api_router


async def lifespan(_: FastAPI):
   Base.metadata.create_all(bind=engine)
   yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)