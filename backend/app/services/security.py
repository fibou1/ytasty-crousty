from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt,JWTError
from fastapi import HTTPException


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
    # On utilise cette pour générer un hash sécurisé du mot de passe (password en plein texte) avant de le stocker dans la base de données.
    return pwd_context.hash(password)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # On utilise cette fonction pour vérifier si le mot de passe en clair (plain_password) correspond au hash stocké (hashed_password).
    return pwd_context.verify(plain_password, hashed_password)

    #doc:https://passlib.readthedocs.io/en/stable/narr/quickstart.html?highlight=pwd_context

# on passe a creation de token pour l'authentification
SECRET_KEY = "votre_cle_secrete_tres_securisee"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



def create_access_token(data: dict) -> str:
    #le dictionnaire data contient les informations que l'on souhaite encoder dans le token (ex: l'ID de l'utilisateur, son rôle, etc.)
    to_encode = data.copy()
    #to_encode est une copie du dictionnaire data pour éviter de modifier l'original. On va y ajouter la date d'expiration du token.
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    #on ajoute la date d'expiration au dictionnaire to_encode sous la clé "exp". Cette date est calculée en ajoutant ACCESS_TOKEN_EXPIRE_MINUTES à l'heure actuelle (en UTC).

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    #on encode le dictionnaire to_encode en un token JWT en utilisant la clé secrète SECRET_KEY et l'algorithme spécifié (HS256). Le résultat est une chaîne de caractères représentant le token JWT.
    return encoded_jwt



def decode_access_token(token: str) -> dict:
    try:
          token_check= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
          return token_check
          print("token est validé")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalide ou expiré")



#doc : https://pypi.org/project/python-jose/
