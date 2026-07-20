from fastapi import FastAPI
from fastapi import APIRouter
from app.routers.produits import routeur 

app = FastAPI()
app.include_router(routeur, prefix="/produits")

@app.get("/")
def hello_world():  
    return {"message": "Bienvenue sur l'API Ytasty Crousty !"}


