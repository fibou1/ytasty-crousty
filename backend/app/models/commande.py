from sqlalchemy import String, Boolean ,Integer ,Time ,ForeignKey ,Float ,Array,DateTime
from sqlalchemy.orm import Mapped , mapped_column
from app.models.base import Base
from datetime import time ,datetime


class commande(Base):
    __tablename__="commande"
    uid_commande: Mapped[str] = mapped_column(String, primary_key=True)
    uid_resto: Mapped[str] = mapped_column(String, ForeignKey("restaurant.uid_resto"), nullable=False)
    num: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    mode_retrait: Mapped[str] = mapped_column(String(200), nullable=False)

    prix_total: Mapped[float] = mapped_column(Float, nullable=False)

    nom_client: Mapped[str] = mapped_column(String(100), nullable=False)
    prenom_client: Mapped[str] = mapped_column(String(100), nullable=False)
    tel_client: Mapped[int] = mapped_column(Integer, nullable=False)
    mail_client: Mapped[str] = mapped_column(String(100), nullable=False)

    date_de_creation: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    #Relationships
    lignes: Mapped[list["LigneCommande"]] = relationship("LigneCommande", back_populates="commande")


class LigneCommande(Base):
    __tablename__="ligne_commande"
    uid_commande: Mapped[str] = mapped_column(String, ForeignKey("commande.uid_commande"), primary_key=True)
    uid_produit: Mapped[str] = mapped_column(String, ForeignKey("produit.uid_produit"), primary_key=True)
    quantite: Mapped[int] = mapped_column(Integer, nullable=False)


    # Relationships
    commande: Mapped["Commande"] = relationship("Commande", back_populates="lignes")
    produit: Mapped["Produit"] = relationship("Produit")