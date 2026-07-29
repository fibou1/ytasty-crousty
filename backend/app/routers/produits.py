from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel

burgers = [
    {"id": 1, "nom": "Crousty Classic", "prix": 10.5},
    {"id": 2, "nom": "Crousty Chicken", "prix": 11.5}
]

class BurgerModele(BaseModel):
    id: int
    nom: str
    prix: float

routeur = APIRouter()

@routeur.get("/menu")
def menu():
    return {"burgers": burgers}

@routeur.post("/menu")
def ajouter_burger(burger: BurgerModele):
    burger_id = len(burgers) + 1
    # On transforme l'objet Pydantic en dictionnaire classique
    burger_dict = burger.model_dump()
    burger_dict["id"] = burger_id
    burgers.append(burger_dict)
    return {"message": "Burger ajouté avec succès", "burger": burger_dict}  



@app.get("/test-db")
def test_database_connection (db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "success"}
    
    except Exception as e:
        raise HTTPException(
         status_code=500, 
         detail=f"Erreur de connexion : {str(e)}"
            )
    

