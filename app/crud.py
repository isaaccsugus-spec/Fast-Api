from sqlalchemy.orm import Session
import models, schemas, utils

# ==========================================
#                 PRODUCTOS
# ==========================================

def obtener_productos(db: Session):
    return db.query(models.Producto).all()

def obtener_producto(db: Session, producto_id: int):
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

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
            setattr(db_producto, var, value) if value is not None else None
        db.commit()
        db.refresh(db_producto)
    return db_producto

def eliminar_producto(db: Session, producto_id: int):
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto


# ==========================================
#                 CATEGORÍAS
# ==========================================

def obtener_categorias(db: Session):
    return db.query(models.Categoria).all()

def obtener_categoria(db: Session, categoria_id: int):
    return db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

def crear_categoria(db: Session, categoria: schemas.CategoriaCreate): 
    db_categoria = models.Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit() 
    db.refresh(db_categoria)
    return db_categoria

def actualizar_categoria(db: Session, categoria_id: int, categoria: schemas.CategoriaCreate):
    db_categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if db_categoria:
        db_categoria.nombre = categoria.nombre
        db.commit()
        db.refresh(db_categoria)
    return db_categoria

def eliminar_categoria(db: Session, categoria_id: int):
    db_categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if db_categoria:
        db.delete(db_categoria)
        db.commit()
    return db_categoria


# ==========================================
#                 USUARIOS
# ==========================================

def obtener_usuarios(db: Session):
    return db.query(models.Usuario).all()

def obtener_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def obtener_usuario_por_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    # Hasheamos la contraseña usando tu función de utils.py
    contrasena_hasheada = utils.hash_password(usuario.password)
    
    # Creamos el modelo usando la contraseña hasheada (¡NUNCA la original en texto plano!)
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        hashed_password=contrasena_hasheada,
        es_admin=usuario.es_admin
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def eliminar_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario

# ==========================================
#                 PEDIDOS
# ==========================================

def crear_pedido(db: Session, pedido: schemas.PedidoCreate, usuario_id: int):
    # 1. Creamos la "factura" en blanco
    db_pedido = models.Pedido(usuario_id=usuario_id)
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    
    # 2. Recorremos el carrito y añadimos las "líneas" a la factura
    for item in pedido.items:
        db_detalle = models.DetallePedido(
            pedido_id=db_pedido.id,
            producto_id=item.producto_id,
            cantidad=item.cantidad
        )
        db.add(db_detalle)
        
        # EXTRAS PARA EL 10: ¡Aquí restarías el stock del producto!
        # producto = db.query(models.Producto).filter(models.Producto.id == item.producto_id).first()
        # producto.en_stock = False (o restar cantidad si tuvieras una columna 'cantidad_stock')
        
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

def obtener_pedidos_usuario(db: Session, usuario_id: int):
    return db.query(models.Pedido).filter(models.Pedido.usuario_id == usuario_id).all()