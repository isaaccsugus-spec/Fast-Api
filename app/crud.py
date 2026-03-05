from sqlalchemy.orm import Session
import models, schemas , utils
from sqlalchemy import or_

# --- PRODUCTOS ---

def obtener_productos(db: Session):
    return db.query(models.Producto).all()

def crear_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.Producto(**producto.model_dump())
    db.add(db_producto)
    db.commit() 
    db.refresh(db_producto) 
    return db_producto

def actualizar_producto(db: Session, producto_id: int, producto: schemas.ProductoCreate):
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if db_producto:
        for var, value in vars(producto).items():
            setattr(db_producto, var, value) if value else None
        db.commit()
        db.refresh(db_producto)
    return db_producto

def eliminar_producto(db: Session, producto_id: int):
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto


# --- CATEGORÍAS ---

# NUEVO: Función para obtener/listar todas las categorías
def obtener_categorias(db: Session):
    return db.query(models.Categoria).all()

def crear_categoria(db: Session, categoria: schemas.CategoriaCreate): 
    db_categoria = models.Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit() 
    db.refresh(db_categoria)
    return db_categoria

# ususarios

def obtener_usuario_por_email(db:Session , email:str) -> Usuario | None:
    return db.query(Usuario).filter(Usuario.email == email).first


def obtener_usuario_por_email(db:Session , usuario_id:str) -> Usuario | None:
    return db.query(Usuario).filter(Usuario.id == email).first

def crear_usuario