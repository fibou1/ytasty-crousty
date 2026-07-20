from sqlalchemy import String, Boolean ,Integer ,Time ,ForeignKey
from sqlalchemy.orm import Mapped , mapped_column
from app.models.base import Base
from datetime import time

class Restaurant(Base):
    __tablename__="restaurant"
    uid_resto: Mapped[str] = mapped_column(String, primary_key=True)
    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    adress: Mapped[str] = mapped_column(String(100), nullable=False)
    status_ouvert: Mapped[bool] = mapped_column(Boolean, default=True)
    horaire_ouverture: Mapped[time] = mapped_column(Time, nullable=False)
    horaire_fermeture: Mapped[time] = mapped_column(Time, nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    numero: Mapped[int] = mapped_column(Integer, nullable=False)
