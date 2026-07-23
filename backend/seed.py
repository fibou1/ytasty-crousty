from app.database import SessionLocal , engine
from app.models import Restaurant
from datetime import time



def seed_restaurants():
    with SessionLocal() as session:
        nombre = session.query(Restaurant).count()
        if nombre >= 3:
            print("c ok Les 3 restaurants sont déjà présents.")
        else:
        # Créer un utilisateur avec des articles
            paris = Restaurant(
            uid_resto="resto1",
            nom="Le Gourmet",
            adress="123 Rue de la Cuisine, Paris",
            status_ouvert=True,
            horaire_ouverture=time(9, 0),
            horaire_fermeture=time(22, 0),
            email="leGourmet@gmail.com",
            numero=123456789
            )
            session.add(paris)
            aix = Restaurant(
            uid_resto="resto2",
            nom="Le Gourmet",
            adress="123 Rue de la Cuisine, Aix-en-Provence",
            status_ouvert=True,
            horaire_ouverture=time(9, 0),
            horaire_fermeture=time(22, 0),
            email="leGourmet@gmail.com",
            numero=123456789
            )
            session.add(aix)
            lyon = Restaurant(
            uid_resto="resto3",
            nom="Le Gourmet",
            adress="123 Rue de la Cuisine, Lyon",
            status_ouvert=True,
            horaire_ouverture=time(9, 0),
            horaire_fermeture=time(22, 0),
            email="leGourmet@gmail.com",
            numero=123456789
            )
            session.add(lyon)
            print(f"Créé : {paris}")
            print(f"Créé : {aix}")
            print(f"Créé : {lyon}")
            session.commit()   
if __name__ == "__main__":
    seed_restaurants()        
        





