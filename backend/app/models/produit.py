from sqlalchemy import String, Boolean ,Integer ,Time ,ForeignKey ,Float ,Array
from sqlalchemy.orm import Mapped , mapped_column
from app.models.base import Base
from datetime import time

class Produit(Base):
    __tablename__="produit"
    uid_produit: Mapped[str] = mapped_column(String, primary_key=True)
    uid_resto: Mapped[str] = mapped_column(String, ForeignKey("restaurant.uid_resto"), nullable=False)

    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    image: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    prix: Mapped[float] = mapped_column(Float, nullable=False)
    dispo: Mapped[bool] = mapped_column(Boolean, nullable=False)
    ingredients: Mapped[list[str]] = mapped_column(ARRAY(String(100)), nullable=False)
