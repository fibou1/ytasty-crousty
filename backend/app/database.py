from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

database_url = "postgresql://admin:admin@postgres:5432/ytasty_db"

engine = create_engine(database_url,pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  Fonction pour injecter la session dans nos routes FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()