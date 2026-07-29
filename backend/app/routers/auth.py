from fastapi import FastAPI , Depends , HTTPException
from fastapi import APIRouter
from pydantic import BaseModel


routeur = APIRouter()

burgers = [
    {"id": 1, "nom": "Crousty Classic", "prix": 10.5},
]

@routeur.post("/auth/login")
def login():
    try:
        # Logique de connexion ici
        return {"message": "Connexion réussie"}
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Erreur lors de la connexion : {str(e)}"
        )

