from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
    # On utilise cette pour générer un hash sécurisé du mot de passe (password en plein texte) avant de le stocker dans la base de données.
    return pwd_context.hash(password)
 def verify_password(plain_password: str, hashed_password: str) -> bool:
    # On utilise cette fonction pour vérifier si le mot de passe en clair (plain_password) correspond au hash stocké (hashed_password).
    return pwd_context.verify(plain_password, hashed_password)

    #doc:https://passlib.readthedocs.io/en/stable/narr/quickstart.html?highlight=pwd_context