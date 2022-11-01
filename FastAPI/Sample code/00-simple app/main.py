from fastapi import FastAPI
from routers import app1

app = FastAPI()

app.include_router(app1.router) # ===> This type of creating application seperately is better for big projects

# define every thing directly is possible in main.py
@app.get('/', tags=["main"])
async def hello():
    return {'message':'Hello!'}