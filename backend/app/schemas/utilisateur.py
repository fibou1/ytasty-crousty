from pydantic import BaseModel, EmailStr,Field

class UtilisateurCreate(BaseModel):
    nom: str = Field(..., min_length=1, max_length=50)
    prenom: str = Field(..., min_length=1, max_length=50)
    email: EmailStr = Field(..., description="Adresse email de l'utilisateur")
    mot_de_passe: str = Field(..., min_length=8, description="Mot de passe de l'utilisateur")
class utilisateurRead(BaseModel):
    uid_user: str
    nom: str
    prenom: str
    email: EmailStr    
    ##indique à Pydantic d'accéder aux valeurs directement via les attributs de l'objet (obj.email) s'il ne reçoit pas un dictionnaire.
    class Config:
        from_attributes = True