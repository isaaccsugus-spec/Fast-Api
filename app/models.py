from sqlalchemy import column ,Integer,String,Float,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categotias(Base):
    __tablename__ ="categorias"
    id = column(Integer,primary_key = True, index=True)
    nombre = column(String, unique=True,index=True)
    productos = relationship("Producto", back_populates="categorias")

class Productos(Base):
    __tablename__ ="Productos"
    id = column(Integer,primary_key = True, index=True)
    nombre=column(String, index=True)
    precio = column(float)
    en_stock = column(Boolean, default=True)
    categoria_id = column(Integer, ForeignKey("categorias.id"))
    Categotia = relationship("Categoria", back_populates="Productos")

class Usuario(Base):
    __tablename__ ="Usuario"
    id = column(Integer,primary_key = True, index=True)
    nombre = column(String, unique=True,index=True)
    email = column(String,unique=True,index= True)
    hashed_password = column(String)

