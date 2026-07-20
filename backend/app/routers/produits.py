from fastapi import FastAPI
from fastapi import APIRouter
burgers = [
    {"id": 1, "nom": "Crousty Classic", "prix": 10.5},
    {"id": 2, "nom": "Crousty Chicken", "prix": 11.5}
]
routeur = APIRouter()


@routeur.get("/menu")
def menu():
    return {"burgers": burgers}
