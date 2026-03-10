from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import DateTime
from datetime import datetime

class Categoria(Base):
    __tablename__ ="categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    productos = relationship("Producto", back_populates="categoria")

class Producto(Base):
    __tablename__ ="Productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Float)
    en_stock = Column(Boolean, default=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categoria = relationship("Categoria", back_populates="productos")

class Usuario(Base):
    __tablename__ ="Usuario"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    es_admin = Column(Boolean, default=False)

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("Usuario.id"))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    
    # Relación: Un pedido pertenece a un usuario, y tiene muchos "detalles"
    usuario = relationship("Usuario")
    detalles = relationship("DetallePedido", back_populates="pedido")

class DetallePedido(Base):
    __tablename__ = "detalles_pedido"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    producto_id = Column(Integer, ForeignKey("Productos.id"))
    cantidad = Column(Integer)
    
    # Relaciones
    pedido = relationship("Pedido", back_populates="detalles")
    producto = relationship("Producto")