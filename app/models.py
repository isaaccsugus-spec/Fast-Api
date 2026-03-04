from sqlalchemy import Column ,Integer,String,Float,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ ="categorias"
    id = Column(Integer,primary_key = True, index=True)
    nombre = Column(String, unique=True,index=True)
    productos = relationship("Producto", back_populates="categorias")

class Productos(Base):
    __tablename__ ="Productos"
    id = Column(Integer,primary_key = True, index=True)
    nombre=Column(String, index=True)
    precio = Column(float)
    en_stock = Column(Boolean, default=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    Categotia = relationship("Categoria", back_populates="Productos")

class Usuario(Base):
    __tablename__ ="Usuario"
    id = Column(Integer,primary_key = True, index=True)
    nombre = Column(String, unique=True,index=True)
    email = Column(String,unique=True,index= True)
    hashed_password = Column(String)

