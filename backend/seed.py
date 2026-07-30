from app.database import SessionLocal , engine
from app.models import Restaurant,User
from datetime import time
from app.services.security import hash_password


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



def seed_users():
    with SessionLocal() as session:
        nombre = session.query(User).count()
        if nombre >= 2:
            print("c ok Les utilisateurs de test sont déjà présents.")
        else:
            user1 = User(
                uid_user="user1",
                uid_resto="resto1",  # Lié au restaurant resto1 créé précédemment
                nom="zidane",
                prenom="zinedine",
                email="zidane.zinedine@example.com",
                address="10 Rue de la france, Paris",
                hash_mdp=hash_password("987654321!"),  # Toujours hacher le mot de passe !
                roles=["user"]
            )

            admin1 = User(
                uid_user="admin1",
                uid_resto=None,
                nom="maitre",
                prenom="gims",
                email="gims.maitre@mail.com",
                address="5 Avenue de Bella, Lyon",
                hash_mdp=hash_password("1223456789"),
                roles=["admin"]
            )

            session.add_all([user1, admin1])
            session.commit()
            print("Utilisateurs de test créés avec succès !")



if __name__ == "__main__":
    seed_restaurants()        
    seed_users()    





