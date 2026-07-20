from fastapi import FastAPI,Depends ,HTTPException
from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.routers.produits import routeur 
from app.database import get_db

app = FastAPI()
app.include_router(routeur, prefix="/produits")

@app.get("/health") 
def health_status():
    return {"status": "healthy"}

@app.get("/")
def hello_world():  
    return {"message": "Bienvenue sur l'API Ytasty Crousty !"}

@app.get("/test-db")
def test_database_connection(db: Session = Depends(get_db)):
    try:
        # ⚙️ On exécute une requête SQL minimale pour tester la liaison
        db.execute(text("SELECT 1"))
        return {"status": "success", "message": "Connexion à PostgreSQL réussie ! 🚀"}
    except Exception as e:
        # 💥 Si ça plante, on renvoie l'erreur précise
        raise HTTPException(
            status_code=500, 
            detail=f"Échec de la connexion à la base de données : {str(e)}"
        )