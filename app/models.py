<<<<<<< HEAD
from sqlalchemy import Column ,Integer,String,Float,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ ="categorias"
    id = Column(Integer,primary_key = True, index=True)
    nombre = Column(String, unique=True,index=True)
=======
from sqlalchemy import column ,Integer,String,Float,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categotias(Base):
    __tablename__ ="categorias"
    id = column(Integer,primary_key = True, index=True)
    nombre = column(String, unique=True,index=True)
>>>>>>> b9f31fd139b225c59d85988d151aece48687f3ba
    productos = relationship("Producto", back_populates="categorias")

class Productos(Base):
    __tablename__ ="Productos"
<<<<<<< HEAD
    id = Column(Integer,primary_key = True, index=True)
    nombre=Column(String, index=True)
    precio = Column(float)
    en_stock = Column(Boolean, default=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
=======
    id = column(Integer,primary_key = True, index=True)
    nombre=column(String, index=True)
    precio = column(float)
    en_stock = column(Boolean, default=True)
    categoria_id = column(Integer, ForeignKey("categorias.id"))
>>>>>>> b9f31fd139b225c59d85988d151aece48687f3ba
    Categotia = relationship("Categoria", back_populates="Productos")

class Usuario(Base):
    __tablename__ ="Usuario"
<<<<<<< HEAD
    id = Column(Integer,primary_key = True, index=True)
    nombre = Column(String, unique=True,index=True)
    email = Column(String,unique=True,index= True)
    hashed_password = Column(String)
=======
    id = column(Integer,primary_key = True, index=True)
    nombre = column(String, unique=True,index=True)
    email = column(String,unique=True,index= True)
    hashed_password = column(String)
>>>>>>> b9f31fd139b225c59d85988d151aece48687f3ba

