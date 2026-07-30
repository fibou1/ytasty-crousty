from fastapi import FastAPI, Depends, HTTPException, APIRouter, status
from pydantic import BaseModel
from app.services.security import verify_password, create_access_token
from app.models.utilisateur import User
from app.database import get_db
from sqlalchemy.orm import Session







routeur2 = APIRouter()

class LoginSchema(BaseModel):
    email: str
    password: str

@routeur2.post("/auth/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    # 1. Recherche de l'utilisateur dans la base de données 
    utilisateur = db.query(User).filter(User.email == data.email).first()
    if utilisateur is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Identifiants incorrects"
        )

    # 2. Vérification du mot de passe 
    if not verify_password(data.password, utilisateur.hash_mdp):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Identifiants incorrects"
        )

    # 3. Génération du jeton JWT 
    token_data = {
        "sub": utilisateur.email, 
        "user_id": utilisateur.uid_user, 
        "roles": utilisateur.roles
    }
    access_token = create_access_token(data=token_data)
    print(f"Token généré pour l'utilisateur {utilisateur.email}: {access_token}")
    return {"access_token": access_token, "token_type": "bearer"}