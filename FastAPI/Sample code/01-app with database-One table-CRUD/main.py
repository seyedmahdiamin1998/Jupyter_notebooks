from fastapi import FastAPI
from database import engine, SessionLocal
import models

from applications.users import users


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Amin")

app.include_router(users.router) 
