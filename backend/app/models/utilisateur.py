from sqlalchemy import String, Boolean ,Integer ,Time ,ForeignKey ,Float ,ARRAY
from sqlalchemy.orm import Mapped , mapped_column
from app.models.base import Base
from datetime import time

class User(Base):
    __tablename__="user"
    uid_user: Mapped[str] = mapped_column(String, primary_key=True)
    uid_resto: Mapped[str | None] = mapped_column(String, ForeignKey("restaurant.uid_resto"), nullable=True)

    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    prenom: Mapped[str] = mapped_column(String(200), nullable=False)
    hash_mdp: Mapped[str] = mapped_column(String(200), nullable=False)
    address: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False)
    roles: Mapped[list[str]] = mapped_column(ARRAY(String(100)), nullable=False)
